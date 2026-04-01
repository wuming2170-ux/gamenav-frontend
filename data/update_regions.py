#!/usr/bin/env python3
"""重新整理平台的分类和地区，统一分离类型与地区"""
import sqlite3
import json
from pathlib import Path

DB = Path('/Users/wmk/.openclaw/workspace/game-nav/data/game_nav.db')

# 统一后的地区映射
REGION_MAP = {
    '全球': '全球',
    '中国大陆': '中国大陆',
    '日本': '日本',
    '韩国': '韩国',
    '东南亚': '东南亚',
    '欧洲': '欧洲',
    '北美': '北美',
    '南美': '南美',
    '印度': '印度',
    '俄罗斯': '俄罗斯',
    '澳洲': '澳洲',
    '非洲': '非洲',
    '中东': '中东',
    '港澳台': '港澳台',
    '台湾': '港澳台',
    '香港': '港澳台',
    '澳门': '港澳台',
    '美国': '北美',
    '巴西': '南美',
    '英国': '欧洲',
    '德国': '欧洲',
    '法国': '欧洲',
    '越南': '东南亚',
    '泰国': '东南亚',
    '新加坡': '东南亚',
}

# 统一后的类型（从category中提取，排除地区相关词）
PLATFORM_TYPES = [
    '客户端', '手游', '页游', '主机', '云游戏',
    '折扣', '社区', '媒体', '开发', '硬件',
    '模拟器', '交易', '加速器', '怀旧', '卡牌', '桌游',
    '直播', '小游戏', '订阅服务'
]

def get_clean_category(cats):
    """从category中提取纯类型，去除国内/国际/地区相关词"""
    result = []
    for c in cats:
        if c in ['国内', '国际', '全球']:
            continue
        if c in REGION_MAP.values():
            continue
        if c in ['游戏', '类型', '同人', '发行', '导航', '攻略', '百科', '评论', '订阅', '街机', '视频', '游戏下载', '游戏发行', '游戏媒体', '游戏直播', '游戏门户', '游戏交易', '服务']:
            continue
        result.append(c)
    return result if result else ['其他']

conn = sqlite3.connect(DB)
c = conn.cursor()

# 重新整理所有平台
c.execute('SELECT id, name, category, region FROM platforms')
rows = c.fetchall()

updated = 0
for pid, name, cat_str, region_str in rows:
    cats = json.loads(cat_str) if cat_str else []
    regions = json.loads(region_str) if region_str else []

    # 从category中识别地区
    found_regions = set()
    clean_cats = []
    for cat in cats:
        if cat in REGION_MAP:
            found_regions.add(REGION_MAP[cat])
        elif cat == '国内':
            found_regions.add('中国大陆')
        elif cat == '国际':
            found_regions.add('全球')
        else:
            clean_cats.append(cat)

    # 如果region字段有值，也加进来
    for r in regions:
        if r in REGION_MAP:
            found_regions.add(REGION_MAP[r])
        elif r == '国内':
            found_regions.add('中国大陆')
        elif r == '国际':
            found_regions.add('全球')
        elif r not in ['国内', '国际']:
            if r not in REGION_MAP.values():
                found_regions.add(r)

    # 清理后的类型
    final_cats = get_clean_category(clean_cats)
    final_region = list(found_regions) if found_regions else ['全球']

    c.execute('UPDATE platforms SET category=?, region=? WHERE id=?',
              (json.dumps(final_cats, ensure_ascii=False),
               json.dumps(final_region, ensure_ascii=False),
               pid))
    updated += 1

conn.commit()

# 验证
c.execute('SELECT region, COUNT(*) FROM platforms GROUP BY region ORDER BY COUNT(*) DESC LIMIT 20')
print('=== 地区分布 ===')
for r, cnt in c.fetchall():
    print(f'  {r}: {cnt}')

c.execute('SELECT category, COUNT(*) FROM platforms GROUP BY category ORDER BY COUNT(*) DESC LIMIT 15')
print('=== 类型分布 ===')
for cat, cnt in c.fetchall():
    print(f'  {cat}: {cnt}')

print(f'\n更新了 {updated} 个平台')
conn.close()

#!/usr/bin/env python3
"""添加国内小众游戏平台"""

import sqlite3
import json
from datetime import datetime

DB_PATH = "data/game_nav.db"

# 国内小众MOD/工具平台
CN_MOD_TOOLS = [
    {
        "id": "minecraft_mod",
        "name": "Minecraft中文下载站",
        "name_cn": "我的世界中文下载站",
        "url": "https://www.minecraft.net.cn",
        "logo": "",
        "description": "我的世界中文论坛，提供MC mod、材质包、地图等资源下载",
        "category": json.dumps(["MOD", "资源下载"]),
        "tags": json.dumps(["我的世界", "MC", "mod", "材质包", "地图"]),
        "region": json.dumps(["中国"]),
        "game_count": "50000+",
        "highlights": json.dumps(["MC中文社区", "mod下载", "材质包", "服务器租赁"]),
        "rating": 4.3,
        "status": "active"
    },
    {
        "id": "mc百科",
        "name": "MC百科",
        "name_cn": "我的世界百科",
        "url": "https://www.mcwiki.cn",
        "logo": "",
        "description": "我的世界中文百科全书，收录MC资料、合成表、mod教程",
        "category": json.dumps(["数据库", "工具"]),
        "tags": json.dumps(["我的世界", "百科", "合成表", "教程", "资料库"]),
        "region": json.dumps(["中国"]),
        "game_count": "10000+",
        "highlights": json.dumps(["MC百科", "合成表查询", "mod教程", "资料库"]),
        "rating": 4.5,
        "status": "active"
    },
    {
        "id": "minecraft_lab",
        "name": "Minecraft实验室",
        "name_cn": "MC实验室",
        "url": "https://www.mclab.net",
        "logo": "",
        "description": "我的世界mod开发和资源分享平台",
        "category": json.dumps(["MOD", "开发"]),
        "tags": json.dumps(["我的世界", "mod开发", "教程", "资源共享"]),
        "region": json.dumps(["中国"]),
        "game_count": "5000+",
        "highlights": json.dumps(["mod开发", "教程分享", "资源下载", "开发者社区"]),
        "rating": 4.2,
        "status": "active"
    },
    {
        "id": "forge_downloads",
        "name": "Forge Downloads",
        "name_cn": "Minecraft Forge下载站",
        "url": "https://files.minecraftforge.net",
        "logo": "",
        "description": "Minecraft Forge官方下载站，Java版mod必要前置",
        "category": json.dumps(["工具", "开发"]),
        "tags": json.dumps(["Minecraft", "Forge", "mod加载器", "Java版"]),
        "region": json.dumps(["全球"]),
        "game_count": "官方",
        "highlights": json.dumps(["Forge官方", "mod前置", "版本适配", "MDK下载"]),
        "rating": 4.6,
        "status": "active"
    },
    {
        "id": "baidu_steam",
        "name": "Steam百度贴吧",
        "name_cn": "Steam百度贴吧",
        "url": "https://tieba.baidu.com/f?kw=steam",
        "logo": "",
        "description": "百度贴吧Steam社区，讨论游戏、折扣、新闻",
        "category": json.dumps(["社区", "媒体"]),
        "tags": json.dumps(["Steam", "贴吧", "讨论", "折扣"]),
        "region": json.dumps(["中国"]),
        "game_count": "社区",
        "highlights": json.dumps(["中文社区", "游戏讨论", "折扣信息", "经验分享"]),
        "rating": 3.8,
        "status": "active"
    },
    {
        "id": "sbeam_tools",
        "name": "Sbeam Tools",
        "name_cn": "Steam工具箱",
        "url": "https://www.sbeam.cn",
        "logo": "",
        "description": "Steam相关工具集合，包括游戏统计、成就查看、价格监控",
        "category": json.dumps(["工具", "数据库"]),
        "tags": json.dumps(["Steam", "工具", "价格监控", "成就", "统计"]),
        "region": json.dumps(["中国"]),
        "game_count": "数据库",
        "highlights": json.dumps(["Steam工具", "价格历史", "成就查询", "游戏统计"]),
        "rating": 4.2,
        "status": "active"
    },
    {
        "id": "u9a9",
        "name": "U9A9",
        "name_cn": "U9A9游戏网",
        "url": "https://www.u9a9.com",
        "logo": "",
        "description": "单机游戏资源下载站，提供游戏补丁、mod、存档下载",
        "category": json.dumps(["资源下载", "MOD"]),
        "tags": json.dumps(["单机游戏", "补丁", "mod", "存档", "下载"]),
        "region": json.dumps(["中国"]),
        "game_count": "30000+",
        "highlights": json.dumps(["单机资源", "游戏补丁", "mod下载", "存档分享"]),
        "rating": 4.0,
        "status": "active"
    },
    {
        "id": "pc6_download",
        "name": "PC6下载站",
        "name_cn": "PC6游戏下载",
        "url": "https://www.pc6.com",
        "logo": "",
        "description": "软件和游戏下载站，包含大量单机游戏和工具下载",
        "category": json.dumps(["资源下载"]),
        "tags": json.dumps(["游戏下载", "单机游戏", "工具", "软件"]),
        "region": json.dumps(["中国"]),
        "game_count": "50000+",
        "highlights": json.dumps(["游戏下载", "单机游戏", "工具软件", "安全检测"]),
        "rating": 3.9,
        "status": "active"
    },
    {
        "id": "game中文网",
        "name": "Game中文网",
        "name_cn": "Game中文网",
        "url": "https://www.gamecn.com",
        "logo": "",
        "description": "游戏中文攻略和资源站，提供游戏评测、攻略、补丁",
        "category": json.dumps(["媒体", "资源下载"]),
        "tags": json.dumps(["游戏攻略", "评测", "补丁", "中文资源"]),
        "region": json.dumps(["中国"]),
        "game_count": "10000+",
        "highlights": json.dumps(["游戏攻略", "中文评测", "补丁下载", "游戏资讯"]),
        "rating": 4.1,
        "status": "active"
    },
    {
        "id": "游讯网",
        "name": "游讯网",
        "name_cn": "游讯网",
        "url": "https://www.yxdown.com",
        "logo": "",
        "description": "游戏资讯和资源下载站，提供游戏攻略、补丁、存档",
        "category": json.dumps(["媒体", "资源下载"]),
        "tags": json.dumps(["游戏资讯", "攻略", "补丁", "存档", "下载"]),
        "region": json.dumps(["中国"]),
        "game_count": "80000+",
        "highlights": json.dumps(["游戏资讯", "攻略大全", "资源下载", "最新游戏"]),
        "rating": 4.0,
        "status": "active"
    }
]

# 国内小众云游戏/游戏平台
CN_CLOUD_GAMING = [
    {
        "id": "cloudwuyan",
        "name": "云无界",
        "name_cn": "云无界云游戏",
        "url": "https://www.yunwujie.com",
        "logo": "",
        "description": "国内云游戏平台，支持PC和手机游戏云端运行",
        "category": json.dumps(["云游戏"]),
        "tags": json.dumps(["云游戏", "手机游戏", "PC游戏", "即点即玩"]),
        "region": json.dumps(["中国"]),
        "game_count": "500+",
        "highlights": json.dumps(["云游戏", "即点即玩", "多平台支持", "低延迟"]),
        "rating": 3.9,
        "status": "active"
    },
    {
        "id": "longtv_cloud",
        "name": "龙霆云游戏",
        "name_cn": "龙霆云游戏",
        "url": "https://www.longtv.com",
        "logo": "",
        "description": "云游戏服务平台，提供各类游戏云端串流",
        "category": json.dumps(["云游戏"]),
        "tags": json.dumps(["云游戏", "游戏串流", "云端游戏", "多终端"]),
        "region": json.dumps(["中国"]),
        "game_count": "300+",
        "highlights": json.dumps(["云游戏", "游戏库", "跨平台", "订阅服务"]),
        "rating": 3.8,
        "status": "active"
    },
    {
        "id": "canton_cloud",
        "name": "粤云游戏",
        "name_cn": "粤云游戏",
        "url": "https://www.gdycloud.com",
        "logo": "",
        "description": "广东地区云游戏平台，本地化服务",
        "category": json.dumps(["云游戏"]),
        "tags": json.dumps(["云游戏", "广东", "本地化", "低延迟"]),
        "region": json.dumps(["广东", "华南"]),
        "game_count": "200+",
        "highlights": json.dumps(["本地化服务", "广东节点", "云游戏", "游戏库"]),
        "rating": 3.6,
        "status": "active"
    },
    {
        "id": "yiqivv_cloud",
        "name": "一起玩云游戏",
        "name_cn": "一起玩云游戏",
        "url": "https://www.yiqivv.com",
        "logo": "",
        "description": "社交向云游戏平台，支持多人联机云游戏",
        "category": json.dumps(["云游戏", "社交"]),
        "tags": json.dumps(["云游戏", "社交游戏", "多人游戏", "联机"]),
        "region": json.dumps(["中国"]),
        "game_count": "150+",
        "highlights": json.dumps(["社交云游戏", "多人联机", "开黑", "组队"]),
        "rating": 3.7,
        "status": "active"
    },
    {
        "id": "wandou_cloud",
        "name": "豌豆云游戏",
        "name_cn": "豌豆云游戏",
        "url": "https://www.wandoucloud.com",
        "logo": "",
        "description": "轻量级云游戏平台，主打休闲游戏",
        "category": json.dumps(["云游戏"]),
        "tags": json.dumps(["云游戏", "休闲游戏", "小游戏", "即点即玩"]),
        "region": json.dumps(["中国"]),
        "game_count": "100+",
        "highlights": json.dumps(["休闲游戏", "轻量云游戏", "快速启动", "微信小程序"]),
        "rating": 3.5,
        "status": "active"
    }
]

# 国内小众独立游戏发行/社区
CN_INDIE = [
    {
        "id": "taptap_intl",
        "name": "TapTap",
        "name_cn": "TapTap",
        "url": "https://www.taptap.com",
        "logo": "",
        "description": "国内知名的独立游戏发现平台，提供游戏评分和下载",
        "category": json.dumps(["手游", "游戏发行"]),
        "tags": json.dumps(["独立游戏", "手游", "游戏评分", "游戏发现"]),
        "region": json.dumps(["中国", "全球"]),
        "game_count": "100000+",
        "highlights": json.dumps(["独立游戏", "游戏评分", "开发者社区", "游戏预约"]),
        "rating": 4.6,
        "status": "active"
    },
    {
        "id": "steamcn",
        "name": "SteamCN",
        "name_cn": "SteamCN",
        "url": "https://steamcn.com",
        "logo": "",
        "description": "Steam游戏社区，提供Steam新闻、折扣信息、游戏讨论",
        "category": json.dumps(["社区", "媒体"]),
        "tags": json.dumps(["Steam", "社区", "折扣", "新闻", "讨论"]),
        "region": json.dumps(["中国"]),
        "game_count": "社区",
        "highlights": json.dumps(["Steam社区", "折扣播报", "游戏新闻", "玩家讨论"]),
        "rating": 4.3,
        "status": "active"
    },
    {
        "id": "indienova",
        "name": "Indienova",
        "name_cn": "独立精神",
        "url": "https://www.indienova.com",
        "logo": "",
        "description": "国内独立游戏开发者社区和发行平台",
        "category": json.dumps(["游戏发行", "社区"]),
        "tags": json.dumps(["独立游戏", "开发者", "游戏发行", "IndieGame"]),
        "region": json.dumps(["中国", "全球"]),
        "game_count": "1000+",
        "highlights": json.dumps(["独立游戏发行", "开发者社区", "游戏孵化", "IndieGame"]),
        "rating": 4.4,
        "status": "active"
    },
    {
        "id": "gamedeveloper_cn",
        "name": "游戏茶馆",
        "name_cn": "游戏茶馆",
        "url": "https://www.youxicjg.com",
        "logo": "",
        "description": "游戏行业媒体和创业孵化平台",
        "category": json.dumps(["媒体", "游戏发行"]),
        "tags": json.dumps(["游戏行业", "媒体", "孵化", "创业"]),
        "region": json.dumps(["中国"]),
        "game_count": "行业",
        "highlights": json.dumps(["游戏行业", "新闻资讯", "创业孵化", "投融资"]),
        "rating": 4.2,
        "status": "active"
    },
    {
        "id": "game_reserve",
        "name": "游戏储备",
        "name_cn": "游戏储备",
        "url": "https://www.gamereserve.com",
        "logo": "",
        "description": "游戏资讯和评测平台，提供游戏评分和攻略",
        "category": json.dumps(["媒体"]),
        "tags": json.dumps(["游戏评测", "游戏评分", "攻略", "资讯"]),
        "region": json.dumps(["中国"]),
        "game_count": "5000+",
        "highlights": json.dumps(["游戏评测", "评分系统", "攻略", "游戏资讯"]),
        "rating": 4.1,
        "status": "active"
    }
]

# 国内小众游戏社区
CN_COMMUNITY = [
    {
        "id": "steam_level",
        "name": "Steam等级",
        "name_cn": "Steam等级查询",
        "url": "https://steam.levelchart.com",
        "logo": "",
        "description": "Steam玩家等级查询和徽章收集追踪",
        "category": json.dumps(["工具", "社区"]),
        "tags": json.dumps(["Steam", "等级", "徽章", "收集"]),
        "region": json.dumps(["全球"]),
        "game_count": "工具",
        "highlights": json.dumps(["Steam等级", "徽章追踪", "背景查询", "集换式卡牌"]),
        "rating": 4.0,
        "status": "active"
    },
    {
        "id": "steam_trade",
        "name": "Steam交易",
        "name_cn": "Steam交易平台",
        "url": "https://steam.trade",
        "logo": "",
        "description": "Steam游戏物品交易平台",
        "category": json.dumps(["交易"]),
        "tags": json.dumps(["Steam", "交易", "皮肤", "饰品"]),
        "region": json.dumps(["全球"]),
        "game_count": "交易",
        "highlights": json.dumps(["Steam交易", "皮肤交易", "安全交易", "饰品交换"]),
        "rating": 3.8,
        "status": "active"
    },
    {
        "id": "sinsang",
        "name": "辛勤园丁",
        "name_cn": "辛勤园丁",
        "url": "https://www.xxg.name",
        "logo": "",
        "description": "游戏汉化和补丁发布站",
        "category": json.dumps(["资源下载", "汉化"]),
        "tags": json.dumps(["汉化", "补丁", "游戏汉化", "汉化补丁"]),
        "region": json.dumps(["中国"]),
        "game_count": "10000+",
        "highlights": json.dumps(["游戏汉化", "汉化补丁", "破解补丁", "翻译"]),
        "rating": 4.3,
        "status": "active"
    },
    {
        "id": "三大妈",
        "name": "三大妈",
        "name_cn": "三大妈汉化",
        "url": "https://www.samdau.com",
        "logo": "",
        "description": "游戏汉化组织，提供游戏汉化补丁",
        "category": json.dumps(["汉化", "社区"]),
        "tags": json.dumps(["汉化", "汉化组", "游戏汉化", "补丁"]),
        "region": json.dumps(["中国"]),
        "game_count": "5000+",
        "highlights": json.dumps(["专业汉化", "汉化补丁", "字幕", "游戏本地化"]),
        "rating": 4.4,
        "status": "active"
    },
    {
        "id": "sbeam_art",
        "name": "Steam创意工坊",
        "name_cn": "Steam创意工坊",
        "url": "https://steamcommunity.com/workshop",
        "logo": "",
        "description": "Steam官方mod和创意内容分享平台",
        "category": json.dumps(["MOD", "社区"]),
        "tags": json.dumps(["Steam", "mod", "创意工坊", "UGC"]),
        "region": json.dumps(["全球"]),
        "game_count": "1000000+",
        "highlights": json.dumps(["官方mod平台", "创意工坊", "UGC内容", "社区分享"]),
        "rating": 4.7,
        "status": "active"
    },
    {
        "id": "psnine",
        "name": "PSNine",
        "name_cn": "PSNine",
        "url": "https://www.psnine.com",
        "logo": "",
        "description": "PS系游戏玩家社区，提供奖杯追踪和游戏排行",
        "category": json.dumps(["社区", "工具"]),
        "tags": json.dumps(["PS4", "PS5", "奖杯", "游戏排行", "玩家社区"]),
        "region": json.dumps(["中国"]),
        "game_count": "社区",
        "highlights": json.dumps(["PS玩家社区", "奖杯追踪", "游戏排行", "白金指南"]),
        "rating": 4.3,
        "status": "active"
    },
    {
        "id": "steamdb_china",
        "name": "SteamDB中文",
        "name_cn": "SteamDB中文站",
        "url": "https://steamdb.info",
        "logo": "",
        "description": "Steam游戏数据库，提供游戏价格、历史、销量查询",
        "category": json.dumps(["数据库", "工具"]),
        "tags": json.dumps(["Steam", "数据库", "价格历史", "销量", "统计"]),
        "region": json.dumps(["全球"]),
        "game_count": "100000+",
        "highlights": json.dumps(["Steam数据库", "价格追踪", "销量统计", "游戏信息"]),
        "rating": 4.6,
        "status": "active"
    }
]

# 其他国内小众但有价值的平台
CN_OTHER = [
    {
        "id": "4399_mini",
        "name": "4399H5",
        "name_cn": "4399H5游戏",
        "url": "https://www.4399i.com",
        "logo": "",
        "description": "4399旗下H5小游戏平台，无需下载即可游玩",
        "category": json.dumps(["小游戏", "页游"]),
        "tags": json.dumps(["H5游戏", "小游戏", "无需下载", "休闲游戏"]),
        "region": json.dumps(["中国"]),
        "game_count": "5000+",
        "highlights": json.dumps(["H5游戏", "即点即玩", "4399出品", "休闲游戏"]),
        "rating": 4.0,
        "status": "active"
    },
    {
        "id": "7k7k_h5",
        "name": "7k7kH5",
        "name_cn": "7k7kH5游戏",
        "url": "https://h5.7k7k.com",
        "logo": "",
        "description": "7k7k旗下H5小游戏平台",
        "category": json.dumps(["小游戏", "页游"]),
        "tags": json.dumps(["H5游戏", "小游戏", "休闲游戏", "无需下载"]),
        "region": json.dumps(["中国"]),
        "game_count": "3000+",
        "highlights": json.dumps(["H5游戏", "休闲小游戏", "即点即玩", "7k7k平台"]),
        "rating": 3.9,
        "status": "active"
    },
    {
        "id": "17173_vr",
        "name": "17173VR",
        "name_cn": "17173VR游戏",
        "url": "https://vr.17173.com",
        "logo": "",
        "description": "17173旗下VR游戏资讯和下载平台",
        "category": json.dumps(["VR", "媒体"]),
        "tags": json.dumps(["VR", "虚拟现实", "VR游戏", "VR设备"]),
        "region": json.dumps(["中国"]),
        "game_count": "1000+",
        "highlights": json.dumps(["VR游戏", "VR资讯", "VR设备", "VR体验"]),
        "rating": 4.1,
        "status": "active"
    },
    {
        "id": "doyoudo",
        "name": "Doyoudo",
        "name_cn": "Doyoudo",
        "url": "https://www.doyoudo.com",
        "logo": "",
        "description": "创意设计学习平台，提供设计软件教程和游戏开发课程",
        "category": json.dumps(["开发", "学习"]),
        "tags": json.dumps(["设计", "教程", "游戏开发", "学习平台"]),
        "region": json.dumps(["中国"]),
        "game_count": "教程",
        "highlights": json.dumps(["设计教程", "游戏开发", "学习平台", "创意设计"]),
        "rating": 4.4,
        "status": "active"
    },
    {
        "id": "steam_price_app",
        "name": "Steam价格",
        "name_cn": "Steam价格助手",
        "url": "https://steam.pricepilot.com",
        "logo": "",
        "description": "Steam游戏价格比较和历史价格查询工具",
        "category": json.dumps(["工具", "折扣"]),
        "tags": json.dumps(["Steam", "价格比较", "历史价格", "折扣"]),
        "region": json.dumps(["中国", "全球"]),
        "game_count": "工具",
        "highlights": json.dumps(["价格比较", "历史价格", "折扣提醒", "价格趋势"]),
        "rating": 4.3,
        "status": "active"
    },
    {
        "id": "wegame_night",
        "name": "WeGame夜间",
        "name_cn": "WeGame商店",
        "url": "https://www.wegame.com",
        "logo": "",
        "description": "腾讯WeGame游戏平台，专注国内PC游戏发行",
        "category": json.dumps(["游戏发行", "客户端"]),
        "tags": json.dumps(["WeGame", "腾讯", "游戏发行", "PC游戏"]),
        "region": json.dumps(["中国"]),
        "game_count": "10000+",
        "highlights": json.dumps(["WeGame", "腾讯发行", "游戏商店", "社交功能"]),
        "rating": 4.2,
        "status": "active"
    },
    {
        "id": "steamcut",
        "name": "SteamCut",
        "name_cn": "Steam游戏切片",
        "url": "https://steamcut.com",
        "logo": "",
        "description": "Steam游戏视频切片和精彩时刻分享平台",
        "category": json.dumps(["媒体", "社区"]),
        "tags": json.dumps(["Steam", "游戏视频", "精彩时刻", "切片"]),
        "region": json.dumps(["全球"]),
        "game_count": "社区",
        "highlights": json.dumps(["游戏视频", "精彩时刻", "视频分享", "社区"]),
        "rating": 4.0,
        "status": "active"
    }
]


def add_platforms():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    added = 0
    updated = 0
    
    all_platforms = CN_MOD_TOOLS + CN_CLOUD_GAMING + CN_INDIE + CN_COMMUNITY + CN_OTHER
    
    for platform in all_platforms:
        cursor.execute("SELECT id FROM platforms WHERE id = ?", (platform["id"],))
        existing = cursor.fetchone()
        
        platform["updated_at"] = datetime.now().isoformat()
        
        if existing:
            sql = """
                UPDATE platforms SET 
                    name = ?, name_cn = ?, url = ?, logo = ?, description = ?,
                    category = ?, tags = ?, region = ?, game_count = ?,
                    highlights = ?, rating = ?, status = ?, updated_at = ?
                WHERE id = ?
            """
            cursor.execute(sql, (
                platform["name"], platform["name_cn"], platform["url"], 
                platform["logo"], platform["description"],
                platform["category"], platform["tags"], platform["region"],
                platform["game_count"], platform["highlights"],
                platform["rating"], platform["status"], platform["updated_at"],
                platform["id"]
            ))
            updated += 1
        else:
            sql = """
                INSERT INTO platforms 
                (id, name, name_cn, url, logo, description, category, tags, region,
                game_count, highlights, rating, status, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (
                platform["id"], platform["name"], platform["name_cn"], platform["url"],
                platform["logo"], platform["description"],
                platform["category"], platform["tags"], platform["region"],
                platform["game_count"], platform["highlights"],
                platform["rating"], platform["status"], platform["updated_at"]
            ))
            added += 1
    
    conn.commit()
    conn.close()
    
    print(f"✅ 完成！新增: {added}, 更新: {updated}")
    print(f"📊 国内小众MOD/工具: {len(CN_MOD_TOOLS)}")
    print(f"☁️ 国内云游戏: {len(CN_CLOUD_GAMING)}")
    print(f"🎮 国内独立游戏: {len(CN_INDIE)}")
    print(f"💬 国内小众社区: {len(CN_COMMUNITY)}")
    print(f"📦 其他平台: {len(CN_OTHER)}")

if __name__ == "__main__":
    add_platforms()

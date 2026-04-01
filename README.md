# 🎮 游戏平台导航 - GameNav

一个全面的游戏平台导航网站，收录 100+ 游戏平台。

## 功能

- 🔍 **搜索** - 支持名称、描述、标签搜索
- 🏷️ **分类筛选** - 按平台类型筛选（客户端/手游/页游/模拟器等）
- 🌐 **地区筛选** - 按覆盖地区筛选
- ⭐ **评分排序** - 按评分高低排序
- 📱 **响应式设计** - 适配手机和电脑
- ⚡ **快速加载** - 支持数据刷新

## 技术栈

- **后端**: FastAPI + SQLite
- **前端**: HTML + TailwindCSS + Vanilla JS
- **爬虫**: Python (可选扩展)

## 快速启动

### 1. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 初始化数据库

```bash
cd backend
python init_db.py
```

### 3. 启动服务

```bash
cd backend
python main.py
```

### 4. 访问

打开浏览器访问: http://localhost:8000

## API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 前端页面 |
| `/api/platforms` | GET | 获取平台列表（支持筛选、分页） |
| `/api/platforms/{id}` | GET | 获取单个平台详情 |
| `/api/stats` | GET | 获取统计信息 |
| `/api/categories` | GET | 获取所有分类 |
| `/api/tags` | GET | 获取所有标签 |

### 查询参数

- `category` - 按分类筛选
- `tag` - 按标签筛选
- `region` - 按地区筛选
- `search` - 搜索关键词
- `sort` - 排序字段 (rating/name)
- `order` - 排序方向 (asc/desc)
- `limit` - 返回数量
- `offset` - 偏移量

## 项目结构

```
game-nav/
├── backend/
│   ├── main.py          # FastAPI 入口
│   ├── database.py       # 数据库配置
│   ├── models.py         # 数据模型
│   ├── init_db.py        # 数据库初始化
│   └── requirements.txt  # 依赖
├── frontend/
│   └── index.html       # 前端页面
└── data/
    └── game_nav.db      # SQLite 数据库
```

## 平台分类

- 🖥️ **客户端平台** - Steam, Epic, GOG, WeGame 等
- 📱 **手游平台** - TapTap, 应用宝, Google Play, App Store 等
- 🎮 **页游平台** - 4399, 7k7k 等
- 🕹️ **模拟器** - PPSSPP, Dolphin, Yuzu 等
- 📰 **游戏媒体** - 游民星空, 3DM, NGA, 机核 等
- 🛠️ **游戏工具** - SteamDB, Steam++, 小黑盒 等
- 💬 **游戏社区** - Discord, Reddit, NGA 等
- 💰 **折扣平台** - 杉果, Humble Bundle, Fanatical 等
- 🚀 **加速器** - 网易UU, 腾讯加速器 等
- 📺 **直播平台** - B站, 斗鱼, 虎牙, Twitch 等
- 🔄 **交易平台** - Steam市场, IGXE 等

## License

MIT

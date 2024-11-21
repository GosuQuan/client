# 🎯 Focus AI - 智能专注力管理系统

<div align="center">
    <img src="docs/images/logo.png" alt="Focus AI Logo" width="200"/>
    <p>利用 AI 提升你的工作效率和专注力 🚀</p>
    <p>
        <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="version 1.0.0"/>
        <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"/>
        <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/>
    </p>
</div>

## ✨ 特性

- 🧠 **AI 辅助** - 智能分析你的工作模式，提供个性化建议
- ⏰ **番茄工作法** - 科学的时间管理方法，提升工作效率
- 📊 **数据分析** - 可视化你的专注度和工作效率
- 🎯 **任务管理** - 智能任务规划和提醒
- 🔄 **习惯养成** - 帮助你建立良好的工作习惯
- 🌙 **全平台支持** - 支持网页端和移动端

## 🚀 快速开始

### 前置要求

- Node.js >= 16
- Python >= 3.8
- PostgreSQL >= 12
- Redis (可选)

### 安装步骤

1. 克隆项目

\`\`\`bash
git clone https://github.com/yourusername/focusai.git
cd focusai
\`\`\`

2. 安装前端依赖

\`\`\`bash
cd client/focus-ai
npm install
\`\`\`

3. 安装后端依赖

\`\`\`bash
cd server
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

4. 配置环境变量

\`\`\`bash
# 前端环境变量
cd client/focus-ai
cp .env.example .env

# 后端环境变量
cd server
cp .env.example .env
\`\`\`

5. 启动服务

\`\`\`bash
# 启动前端
cd client/focus-ai
npm start

# 启动后端
cd server
python app/main.py
\`\`\`

## 🏗 技术架构

### 前端

- React 18
- Ant Design 5
- Framer Motion
- Redux Toolkit
- React Router 6

### 后端

- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- JWT Authentication

## 📱 界面预览

<div align="center">
    <img src="docs/images/dashboard.png" alt="Dashboard" width="80%"/>
    <p><em>仪表盘界面</em></p>
</div>

## 🔧 开发指南

### 目录结构

\`\`\`
focusai/
├── client/                # 前端代码
│   ├── src/              # 源代码
│   ├── public/           # 静态资源
│   └── package.json      # 依赖配置
├── server/               # 后端代码
│   ├── app/             # 应用代码
│   │   ├── api/        # API 路由
│   │   ├── core/       # 核心功能
│   │   ├── models/     # 数据模型
│   │   └── main.py     # 入口文件
│   ├── tests/          # 测试文件
│   └── requirements.txt # Python 依赖
├── docs/                # 文档
│   └── images/         # 文档图片
└── README.md           # 项目说明
\`\`\`

## 📄 开源协议

本项目采用 MIT 协议 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [React](https://reactjs.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Ant Design](https://ant.design/)
- [Framer Motion](https://www.framer.com/motion/)

## 📞 联系我们

- Website: [https://focusai.dev](https://focusai.dev)
- Email: contact@focusai.dev
- Twitter: [@focusai](https://twitter.com/focusai)

---

<div align="center">
    <p>如果这个项目对你有帮助，请给它一个 ⭐️</p>
    <p>Made with ❤️ by Focus AI Team</p>
</div>

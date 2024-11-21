# Focus AI Backend

Focus AI 是一个基于 FastAPI 的后端服务，提供 AI 相关功能的 RESTful API。

## 技术栈

- Python 3.11
- FastAPI
- MySQL
- SQLAlchemy
- JWT Authentication

## 环境要求

- Python 3.11+
- MySQL 9.0+
- 虚拟环境 (venv)

## 安装步骤

### 1. 克隆项目

```bash
git clone <repository_url>
cd focusAI/server
```

### 2. 创建并激活虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
```

### 3. 安装依赖

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. 安装并配置 MySQL

如果你使用 macOS 和 Homebrew：

```bash
# 安装 MySQL
brew install mysql

# 启动 MySQL 服务
brew services start mysql

# 创建数据库
mysql -u root -e "CREATE DATABASE IF NOT EXISTS focus_ai;"
```

### 5. 配置环境变量

创建 `.env` 文件并设置以下变量：

```ini
# Database configuration
DATABASE_URL=mysql+pymysql://root@localhost/focus_ai

# JWT configuration
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS configuration
ALLOWED_ORIGINS=http://localhost:3000
```

## 启动服务器

```bash
uvicorn app.main:app --reload --port 8001
```

## 常见问题及解决方案

### 1. ModuleNotFoundError: No module named 'fastapi'

**解决方案**：确保在激活的虚拟环境中安装了所有依赖：
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 2. ImportError: email-validator is not installed

**解决方案**：安装 email-validator 包：
```bash
pip install email-validator
```

### 3. MySQL 连接错误

如果遇到 "Can't connect to MySQL server on 'localhost'" 错误：

**解决方案**：
1. 确保 MySQL 服务正在运行：
   ```bash
   brew services start mysql
   ```
2. 检查 MySQL 服务状态：
   ```bash
   brew services list
   ```
3. 验证数据库是否存在：
   ```bash
   mysql -u root -e "SHOW DATABASES;"
   ```

### 4. 依赖包版本冲突

如果遇到依赖包版本冲突，建议按以下顺序安装核心依赖：

```bash
pip install fastapi uvicorn[standard]
pip install sqlalchemy pymysql
pip install python-jose[cryptography] passlib[bcrypt]
pip install python-multipart python-dotenv
pip install email-validator pydantic-settings
```

## API 文档

启动服务器后，可以通过以下 URL 访问 API 文档：

- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

## 项目结构

```
server/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       └── endpoints/
│   │           └── auth.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── session.py
│   ├── models/
│   │   └── user.py
│   └── services/
│       └── auth.py
├── .env
├── requirements.txt
└── README.md
```

## 开发指南

1. 所有新的 API 端点应该添加到 `app/api/v1/endpoints/` 目录下
2. 数据库模型定义在 `app/models/` 目录下
3. 业务逻辑应该放在 `app/services/` 目录下
4. 配置相关的代码放在 `app/core/` 目录下

## 安全注意事项

1. 永远不要在代码中硬编码敏感信息
2. 所有的密码都应该使用 bcrypt 进行哈希处理
3. 使用 JWT 进行身份验证
4. 正确配置 CORS 以防止未授权的跨域请求

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

[许可证类型]

## 联系方式

[联系信息]

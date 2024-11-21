#!/bin/bash

# 检查 Python 3.11 是否安装
if ! command -v python3.11 &> /dev/null; then
    echo "Python 3.11 is not installed. Please install it first."
    exit 1
fi

# 检查虚拟环境是否存在
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3.11 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "Installing dependencies..."
pip install -r requirements.txt

# 启动服务器
echo "Starting server..."
uvicorn app.main:app --reload --port 8003
# 🎮 GameSense AI

> AI-powered Game Assistant Agent  
> 基于大语言模型的智能游戏助手 Agent


## 📖 Introduction | 项目介绍


### English

GameSense AI is an AI-powered game assistant built with Large Language Models (LLM).

It helps players analyze game strategies, search game knowledge, generate personalized gameplay suggestions, and automatically create game-related content.

The project combines Agent workflow, RAG (Retrieval-Augmented Generation), and LLM-based content generation to provide an intelligent gaming companion.


### 中文

GameSense AI 是一个基于大语言模型构建的 AI 游戏助手。

它可以帮助玩家：

- 查询游戏攻略
- 分析 Boss 机制
- 获取个性化打法建议
- 自动生成游戏内容文章

项目结合了：

- AI Agent 工作流
- RAG 检索增强生成
- 大语言模型内容生成

实现一个面向玩家和游戏内容创作者的智能助手。



---

# ✨ Features | 功能特点


## 1. 🎯 Game Strategy Assistant | 游戏攻略助手

### English

Users can ask questions about games, and the AI will analyze:

- Boss mechanics
- Recommended equipment
- Combat strategies
- Beginner-friendly tips


### 中文

用户可以输入游戏问题，例如：
黑神话悟空虎先锋怎么打？

AI 会自动分析：

- Boss技能机制
- 战斗策略
- 装备推荐
- 新手打法



---


## 2. 📚 RAG Knowledge Retrieval | 游戏知识库检索


### English

The system uses RAG technology to retrieve relevant game information from a local knowledge base before generating answers.


### 中文

系统使用 RAG 技术：

流程：
User Question

  ↓

Vector Search

  ↓

Game Knowledge Database

  ↓

LLM Generation

  ↓

AI Answer



Implemented with:

- Chroma Vector Database
- BGE Embedding Model



---


## 3. ✍️ AI Content Writer | AI内容创作


### English

GameSense AI can generate different types of gaming content:


- Xiaohongshu game guides
- Bilibili video scripts
- Game reviews


### 中文

支持多种内容生成模式：


### 小红书攻略

生成：

- 吸引人的标题
- Emoji风格正文
- 游戏标签


### B站视频脚本

生成：

- 开场吸引点
- 游戏介绍
- 攻略流程
- 总结


### 游戏测评文章

生成：

- 游戏背景
- 玩法分析
- 优缺点评价



---


# 🛠️ Tech Stack | 技术栈


## Backend

- Python
- FastAPI
- LangChain
- ChromaDB
- DeepSeek API


## Frontend

- Vue3
- Vite
- Axios


## AI

- LLM API
- RAG
- Agent Workflow
- Embedding Model



---


# 📂 Project Structure | 项目结构



GameSense-AI

│
├── backend
│
│ ├── main.py # FastAPI server
│ ├── agent.py # AI Agent workflow
│ ├── rag.py # RAG retrieval
│ ├── search.py # Web search tool
│ ├── writer.py # Content generation module
│ ├── llm.py # LLM configuration
│ ├── knowledge # Game knowledge files
│ └── vector_db # Chroma database
│
│
└── frontend
│
├── src
│ └── App.vue
│
├── package.json
└── vite.config.js




---


# ⚙️ Installation | 环境安装


## 1. Clone Repository


```bash
git clone https://github.com/your-name/GameSense-AI.git

cd GameSense-AI
```
## Backend Setup | 后端配置

Enter backend:

cd backend

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a file:

.env

Add your own API keys:

DEEPSEEK_API_KEY=your_api_key_here

SERPAPI_KEY=your_serpapi_key_here

# ⚠️ Important:

Do NOT upload your real API keys to GitHub.

Replace them with your own keys before running the project.

注意：

请不要将真实 API Key 上传到 GitHub。

用户需要自行申请并填写：

大模型 API Key
搜索 API Key
## Frontend Setup | 前端配置

Enter frontend:

cd frontend

Install dependencies:

npm install
## 🚀 Running the Project | 启动项目
Method 1: Manual Start
Start Backend
cd backend

uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000
Start Frontend
cd frontend

npm run dev

Frontend runs at:

http://localhost:5173
Method 2: One-click Launch

Run:

start_GameSense_AI.bat

The script will automatically:

Start backend server
Start frontend server
Open browser
## 💡 Usage | 使用方法

Open browser:

http://localhost:5173

Select a mode:

Chat Mode

Example:

黑神话悟空虎先锋怎么打？
Writing Mode

Example:

生成一篇黑神话悟空虎先锋小红书攻略

The AI will automatically generate game content.

# ⚠️ Notes | 注意事项
API Key is required.
Do not upload .env file containing real keys.
First RAG initialization may download embedding models, which may take some time.
Internet connection is required for:
LLM API
Web search function
# 📌 Future Improvements | 后续计划
User gaming profile memory
Personalized recommendation
More game knowledge databases
Multi-agent collaboration
Mobile application

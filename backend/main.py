from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from writer import generate_content

from agent import game_agent


# 创建FastAPI应用

app = FastAPI(
    title="GameSense AI",
    description="AI 游戏攻略助手",
    version="1.0"
)



# ===============================
# 允许Vue前端访问
# ===============================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



# ===============================
# 请求数据格式
# ===============================

class ChatRequest(BaseModel):

    question: str



# ===============================
# 首页测试
# ===============================

@app.get("/")
def home():

    return {

        "project": "GameSense AI",

        "status": "running",

        "docs": "/docs"

    }



# ===============================
# AI聊天接口
# ===============================

@app.post("/chat")
def chat(request: ChatRequest):


    print("收到问题:", request.question)


    answer = game_agent(

        request.question

    )


    return {

        "answer": answer

    }


class WriteRequest(BaseModel):

    content_type:str

    game_info:str

    user_level:str="新手"




@app.post("/write")
def write(request:WriteRequest):


    result = generate_content(

        request.content_type,

        request.game_info,

        request.user_level

    )


    return {

        "content":result

    }
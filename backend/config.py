# config.py

import os

from dotenv import load_dotenv


# 加载.env
load_dotenv()



# DeepSeek API Key

DEEPSEEK_API_KEY = os.getenv(
    "DEEPSEEK_API_KEY"
)



# SerpAPI搜索Key

SERPAPI_KEY = os.getenv(
    "SERPAPI_KEY"
)



# DeepSeek模型

MODEL_NAME = "deepseek-chat"



# API地址

BASE_URL = "https://api.deepseek.com"
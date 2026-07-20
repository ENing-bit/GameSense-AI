from langchain_openai import ChatOpenAI


from config import (
    DEEPSEEK_API_KEY,
    BASE_URL,
    MODEL_NAME
)



llm = ChatOpenAI(

    model=MODEL_NAME,

    api_key=DEEPSEEK_API_KEY,

    base_url=BASE_URL,

    temperature=0.7

)
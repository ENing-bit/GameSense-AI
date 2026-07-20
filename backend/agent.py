from langchain.agents import create_agent


from llm import llm


from tools import (
    knowledge_search,
    web_game_search
)



# Agent拥有的工具

tools = [

    knowledge_search,

    web_game_search

]



# 创建Agent


agent = create_agent(

    model=llm,

    tools=tools,


    system_prompt="""

你是 GameSense AI，
一个专业的游戏攻略助手。


你的工作流程：

1. 优先查询本地游戏知识库。
2. 如果知识库没有相关信息，
   再使用互联网搜索工具。
3. 综合资料生成详细攻略。


回答要求：

- 分析BOSS机制
- 给出操作建议
- 推荐装备技能
- 根据玩家水平调整难度


回答要像专业游戏攻略作者。


"""

)



def game_agent(question:str):


    result = agent.invoke(

        {

            "messages":[

                {

                    "role":"user",

                    "content":question

                }

            ]

        }

    )


    return result["messages"][-1].content
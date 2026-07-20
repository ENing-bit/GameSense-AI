from langchain.tools import tool

from search import web_search

from rag import search_knowledge



@tool
def knowledge_search(query:str):
    """
    查询游戏知识库。
    用于查询已有游戏资料，
    例如BOSS机制、装备、技能、攻略等。
    """

    result = search_knowledge(query)

    return result



@tool
def web_game_search(query:str):
    """
    搜索互联网最新游戏资料。
    用于查询版本更新、最新攻略等。
    """

    results = web_search(query)


    text = ""


    for item in results:

        text += f"""
标题:
{item['title']}

摘要:
{item['snippet']}

链接:
{item['link']}

"""


    return text
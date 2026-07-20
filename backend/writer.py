from llm import llm



def generate_content(
        content_type,
        game_info,
        user_level="新手"
):


    if content_type == "xiaohongshu":

        prompt=f"""

你是一名专业游戏内容创作者。

请根据以下游戏资料，
生成小红书风格攻略。


游戏资料：

{game_info}


玩家水平：

{user_level}


要求：

1. 标题吸引人
2. 使用emoji
3. 分模块介绍
4. 给出具体打法
5. 添加热门标签


格式：

标题：

正文：

标签：

"""



    elif content_type == "video":

        prompt=f"""

你是一名B站游戏UP主。

根据下面资料生成视频脚本。


资料：

{game_info}


要求：

包含：

1. 开场吸引点
2. Boss介绍
3. 技能机制
4. 实战打法
5. 总结


"""



    elif content_type == "review":

        prompt=f"""

你是一名游戏测评作者。

根据资料写游戏分析文章。


资料：

{game_info}


包含：

游戏背景

玩法分析

优缺点

玩家推荐


"""



    else:

        prompt=f"""

生成游戏攻略：

{game_info}

"""



    response = llm.invoke(prompt)


    return response.content
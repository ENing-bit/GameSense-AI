# search.py


from serpapi import GoogleSearch


from config import SERPAPI_KEY




def web_search(query:str):


    print(
        "正在搜索:",
        query
    )


    params={


        "engine":
        "google",


        "q":
        query,


        "api_key":
        SERPAPI_KEY,


        "num":
        5

    }



    search = GoogleSearch(params)


    result = search.get_dict()



    articles=[]



    for item in result.get(
        "organic_results",
        []
    ):


        articles.append(


            {


            "title":
            item.get(
                "title",
                ""
            ),



            "snippet":
            item.get(
                "snippet",
                ""
            ),



            "link":
            item.get(
                "link",
                ""
            )


            }

        )



    return articles
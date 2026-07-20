import os

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import TextLoader



VECTOR_DB="vector_db"




def build_vector_db():


    documents=[]


    for file in os.listdir("knowledge"):


        path="knowledge/"+file


        loader=TextLoader(
            path,
            encoding="utf-8"
        )


        documents.extend(
            loader.load()
        )



    splitter=RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50

    )


    docs=splitter.split_documents(
        documents
    )


    embeddings=HuggingFaceEmbeddings(

        model_name=
        "BAAI/bge-small-zh"

    )


    db=Chroma.from_documents(

        docs,

        embeddings,

        persist_directory=VECTOR_DB

    )


    db.persist()



    print("知识库建立完成")





def search_knowledge(query):


    embeddings=HuggingFaceEmbeddings(

        model_name=
        "BAAI/bge-small-zh"

    )


    db=Chroma(

        persist_directory=VECTOR_DB,

        embedding_function=embeddings

    )


    result=db.similarity_search(

        query,

        k=3

    )


    return "\n".join(

        [
            r.page_content
            for r in result
        ]

    )
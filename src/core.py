from langchain_groq import ChatGroq
from langchain_classic.prompts import PromptTemplate

def create_llm(groq_api_key):
    """
    Создание LLM
    
    :param groq_api_key: API-KEY Groq

    Returns:
        chain:Готовая до роботы LLM
    """

    llm = ChatGroq(
        model='',
        temperature=0,
        groq_api_key=groq_api_key
    )

    prompt = PromptTemplate(
        input_variables=['loader_video'],
        template="""Ты ИИ-Агент по анализу видео из Youtube.
        Твоя задача давать краткий отчёт о видео
        
        Видео:{loader_video}"""
    )

    chain = prompt | llm

    return chain

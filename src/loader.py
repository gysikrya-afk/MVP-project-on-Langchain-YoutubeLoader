from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def youtube_loader(url_video):
    """
    Загрузка видео из Youtube
    
    :param url_video: Url адрес видео

    Returns:
        docs:Готовая загрузка
    """

    loader = YoutubeLoader(
        video_id=url_video,
        add_video_info=True,
        language=['en','ru','uk']
    )

    docs = loader.load()

    return docs

def text_splitter(docs):
    """
    Разбитие текста на чанки
    
    :param docs:Загруженный документ

    Returns:
        split_docs:Разделённый документ на чанки
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300
    )

    split_docs = splitter.split_documents(docs)

    return split_docs

from sqlalchemy.orm import Session
from models import NewsArticle, NewsSource
from datetime import datetime


def insert_raw_to_db(session: Session, raw_article: dict):
    source = raw_article.pop("source")
    processed_date = datetime.fromisoformat(raw_article['publishedAt'])
    raw_article['publishedAt'] = processed_date.strftime('%Y-%m-%d %H:%M:%S')
    source_model = NewsSource(**source)
    article_model = NewsArticle(**raw_article)

    try:
        session.add(article_model)
        session.add(source_model)
        session.commit()
        return 0
    except Exception as e:
        print(e)
        return 1
    

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NewsSource(Base):
    __tablename__ = 'news_source'

    id = Column(String(100), primary_key=True)
    name = Column(String(255), nullable=False)

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    content = Column(Text)
    author = Column(String(100))
    publishedAt = Column(DateTime)
    url = Column(Text)
    urlToImage = Column(Text)

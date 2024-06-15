from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configure the database connection URL
db_url = 'mysql+pymysql://root:@127.0.0.1:3306/news_scraper_db'

Base = declarative_base()
# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create a session factory
session = sessionmaker(bind=engine)()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure the database connection URL
db_url = 'mysql+mysqlconnector://root:@localhost:3306/news_scraper_db'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)

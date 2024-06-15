import requests
# from news_scraper.news_dataclasses import NewsArticle
from models import NewsArticle
# from models import NewsArticle as news_model
from database import session
from utils import insert_raw_to_db
base_url = "https://newsapi.org/v2/top-headlines?"

api_key = "782eda317e354a6ebca1afd09ec5f23e"

url = base_url + "sources=bbc-news"
url += "&" + f"apiKey={api_key}"
response = requests.get(url)

articles = response.json().get("articles")

resp = insert_raw_to_db(session, articles[0])
print(resp)


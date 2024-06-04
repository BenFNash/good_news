import requests
from news_scraper.news_dataclasses import NewsArticle
base_url = "https://newsapi.org/v2/top-headlines?"

api_key = "782eda317e354a6ebca1afd09ec5f23e"

url = base_url + "sources=bbc-news"
url += "&" + f"apiKey={api_key}"
response = requests.get(url)

articles = response.json().get("articles")

article = NewsArticle(**articles[0])
print(article)

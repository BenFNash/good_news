from dataclasses import dataclass, asdict

@dataclass
class NewsSource:
    id: str
    name: str

@dataclass
class NewsArticle:
    source: NewsSource
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str
    
    def __post_init__(self):
        self.source = NewsSource(**self.source)

    def dict(self):
        return {k: v for k, v in asdict(self).items()}

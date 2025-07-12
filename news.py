from bs4 import BeautifulSoup as BS
import requests

class NewsScraper:
    def __init__(self):
        self.overall_news = {}

    def fetch_moneycontrol(self):
        try:
            url = "https://www.moneycontrol.com/news/business/stocks/"
            page = requests.get(url)
            soup = BS(page.content, "html.parser")
            news_items = soup.find_all("li", class_="clearfix")
            for i, news in enumerate(news_items):
                if i <= 1:
                    headline = news.get_text().strip()
                    self.overall_news[headline] = "Moneycontrol"
        except Exception as e:
            print("Unable to fetch data from Moneycontrol. Error:", e)

    def fetch_cnbc(self):
        try:
            url = "https://www.cnbctv18.com/market/"
            page = requests.get(url)
            soup = BS(page.content, "html.parser")
            news_items = soup.find_all("h3", class_="jsx-f14ac246253a1b7d")
            for i, news in enumerate(news_items):
                if i <= 1:
                    headline = news.get_text().strip()
                    self.overall_news[headline] = "CNBC"
        except Exception as e:
            print("Unable to fetch data from CNBC. Error:", e)

    def get_all_news(self):
        self.fetch_cnbc()
        self.fetch_moneycontrol()
        return self.overall_news



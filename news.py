# from bs4 import BeautifulSoup as BS
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# class NewsScraper:
#     def __init__(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--window-size=1920x1080")
#
#         self.driver = webdriver.Chrome(options=chrome_options)
#         self.overall_news = []
#
#     def fetch_moneycontrol(self):
#         try:
#             url = "https://www.moneycontrol.com/news/business/stocks/"
#             page = requests.get(url)
#             soup = BS(page.content, "html.parser")
#             news_items = soup.find_all("li", class_="clearfix")
#             for i, news in enumerate(news_items):
#                 if i <=1:
#                     self.overall_news.append(f"{news.get_text().strip()} | Moneycontrol")
#         except Exception as e:
#             print("Unable to fetch data from Moneycontrol. Error:", e)
#
#     def fetch_business_standard(self):
#         try:
#             url = "https://www.business-standard.com/"
#             self.driver.get(url)
#             news_items = self.driver.find_elements(By.CLASS_NAME, "cardlist")
#             for i,news in enumerate(news_items):
#                 if i <= 1:
#                     cleaned = news.text.strip().replace("\n", "").replace("premium", "")
#                     for x in ["2 min read", "3 min read", "4 min read", "5 min read"]:
#                         cleaned = cleaned.replace(x, "")
#                         self.overall_news.append(f"{cleaned} | Business Standard")
#         except Exception as e:
#             print("Unable to fetch data from Business Standard. Error:", e)
#
#     def fetch_livemint(self):
#         try:
#             url = "https://www.livemint.com/latest-news"
#             self.driver.get(url)
#             news_items = self.driver.find_elements(By.CLASS_NAME, "listingNew")
#             for i,news in enumerate(news_items):
#                 if i <=1:
#                     self.overall_news.append(f"{news.text.strip().replace("\n", "")} | Livemint")
#         except Exception as e:
#             print("Unable to fetch data from LiveMint. Error:", e)
#
#     def fetch_cnbc(self):
#         try:
#             url = "https://www.cnbctv18.com/market/"
#             page = requests.get(url)
#             soup = BS(page.content, "html.parser")
#             news_items = soup.find_all("h3", class_="jsx-f14ac246253a1b7d")
#             for i,news in enumerate(news_items):
#                 if i <=1:
#                     self.overall_news.append(f"{news.get_text()} | CNBC")
#         except Exception as e:
#             print("Unable to fetch data from CNBC. Error:", e)
#
#     def get_all_news(self):
#         self.fetch_moneycontrol()
#         self.fetch_business_standard()
#         self.fetch_livemint()
#         self.fetch_cnbc()
#         self.driver.quit()
#         return self.overall_news
#
# n1 = NewsScraper()
# news = n1.get_all_news()
# for n in news:
#     print(n)
# print(len(news))

from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class NewsScraper:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument("--user-data-dir=/tmp/unique-profile")

        self.driver = webdriver.Chrome(options=chrome_options)
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

    def fetch_business_standard(self):
        try:
            url = "https://www.business-standard.com/"
            self.driver.get(url)
            news_items = self.driver.find_elements(By.CLASS_NAME, "cardlist")
            for i, news in enumerate(news_items):
                if i <= 1:
                    cleaned = news.text.strip().replace("\n", "").replace("premium", "")
                    for x in ["2 min read", "3 min read", "4 min read", "5 min read"]:
                        cleaned = cleaned.replace(x, "")
                    self.overall_news[cleaned] = "Business Standard"
        except Exception as e:
            print("Unable to fetch data from Business Standard. Error:", e)

    def fetch_livemint(self):
        try:
            url = "https://www.livemint.com/latest-news"
            self.driver.get(url)
            news_items = self.driver.find_elements(By.CLASS_NAME, "listingNew")
            for i, news in enumerate(news_items):
                if i <= 1:
                    headline = news.text.strip().replace("\n", "")
                    self.overall_news[headline] = "Livemint"
        except Exception as e:
            print("Unable to fetch data from LiveMint. Error:", e)

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
        self.fetch_livemint()
        self.fetch_business_standard()
        self.fetch_moneycontrol()
        self.driver.quit()
        return self.overall_news



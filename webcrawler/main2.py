import urllib.request as urllib2
from bs4 import BeautifulSoup


class WebCrawler:

    def __init__(self, keywords, pages=0, search_engine="google"):
        self.__keywords = keywords
        self.__pages = (pages+1)
        self.__search_engine = search_engine

    def __pagination_list_generator(self):
        return list(range(0, self.__pages*10, 10))

    def __google_url_generator(self):

        if self.__pages != 0:
            url_generator_as_pagination()

    def url_generator_as_pagination(self):
        pass


if __name__ == "__main__":
    pages = 5
    keywords = "love"
    search_engine = "google"
    webcrawler = WebCrawler(
        keywords=keywords,
        pages=pages,
        search_engine=search_engine)

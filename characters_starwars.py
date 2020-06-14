import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_Star_Wars_characters']

    def parse(self, response):
        for title in response.css('div#mw-content-text tr'):
            yield {'character': title.css('a ::text').get()}

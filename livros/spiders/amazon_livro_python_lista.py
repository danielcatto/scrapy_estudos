import scrapy
import re
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "amazon_lista"
    start_urls = [
                    'https://www.amazon.com.br/s/ref=nb_sb_noss?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=python'    ]


    def parse(self, response):
        sel = response.css('div.a-row h2::text')[0].extract()
        for produtos in sel:
            print(produtos)

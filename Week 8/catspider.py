# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request

class CatSpider(scrapy.Spider):
    name = "cats"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_cat_breeds'
    ]

    def parse(self, response):
        rows = response.css('table.wikitable tr')
        for row in rows[1:]:
            data = row.css("td")
            d = {
                'breed': data[0].css("::text").extract_first(),
                'country': data[1].css("::text").extract_first(),
                'origin': data[2].css("::text").extract_first(),
                'coat': data[4].css("::text").extract_first(),
                'pattern': data[5].css("::text").extract_first()
            }
            yield d            
            
        
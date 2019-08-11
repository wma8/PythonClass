# -*- coding: utf-8 -*-

import scrapy

class CatSpider2(scrapy.Spider):
    name = "cats2"
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
            rel_url = data[0].css("a::attr(href)").extract_first()
            full_url = response.urljoin(rel_url)
            yield scrapy.Request(full_url,self.parse2, meta = {"item":d})           

    def parse2(self,response):
        d = response.meta["item"]
        paragraphs = response.css("div#mw-content-text p")
        paragraph = paragraphs[0]
        description = "".join(paragraph.css("::text").extract())
        d["description"] = description
        yield d
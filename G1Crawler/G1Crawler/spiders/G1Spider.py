# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import scrapy
import sys

class G1spiderSpider(scrapy.Spider):
    name = 'G1Spider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia/']

    def parse(self, response):
        news_list = response.css('.bastian-page .bastian-feed-item')
        
        for news in news_list:
             title = news.css('.feed-post-link::text').extract_first()
             description =  news.css('.feed-post-body-resumo::text').extract_first()
             image_url = news.css('.bstn-fd-picture-image::attr(src)').extract_first()
             link = news.css('.feed-post-link::attr(href)').extract_first()
            
             
             yield({'title':title, 'description':description, 'image_url':image_url, 'link':link})

           



import scrapy
import pandas as pd 
import time
class edmunds(scrapy.Spider):
    http_user='someuser'
    http_pass='somepass'
    name='car'
    u='https://www.edmunds.com/car-incentives'
    start_urls=[
        'https://www.edmunds.com/car-incentives/'
    ]
    def parse(self, response):
        
        for cars in response.css('a.text-primary-darker::attr(href)'):
            url = response.urljoin(cars.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self, response):
        name=response.css('h1.heading-2.mb-1_5::text').get()
        for links in response.css('a.incentives-link.text-primary-darker.d-flex.flex-column.h-100::attr(href)'):
            url=response.urljoin(links.extract())
            yield scrapy.Request(url, callback = self.final_parse)
    
    def final_parse(self,response):
        #i=0
        for value in response.css('li.unordered-list-item'):
            #value.css('span::text').get()
            yield{
                'name':self.name,
                'model':value.css('h1.heading-2.mb-1_5::text').get()
                #f'data[i]':value.css('span::text').get()[i]
            }
            #i=i+1

#kira
import scrapy
import pandas as pd 
class car(scrapy.Spider):
    http_user='someuser'#imp shit if you skip u get dns error
    http_pass='somepass'
    name='edmund'#name of spider
    start_urls=['https://www.edmunds.com/car-incentives/']
    def parse(self, response):   
        for cars in response.css('a.text-primary-darker::attr(href)'):
            url = response.urljoin(cars.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)#going to next page

    def parse_dir_contents(self, response):
        for links in response.css('a.incentives-link.text-primary-darker.d-flex.flex-column.h-100::attr(href)'):
            url=response.urljoin(links.extract())
            yield scrapy.Request(url, callback = self.final_parse)#going to next page
    def final_parse(self,response):
        self.Student=[]
        self.military=[]
        self.First_Responder=[]
        self.Customer_Bonus=[]
        self.Loyalty=[]
        self.Conquest=[]
        self.Mobility=[]
        self.offers=response.css('li.unordered-list-item')
        self.cash_offers=self.offers.css('span::text').getall()
        for self.offer in self.cash_offers:
            if 'Lease' in self.offer:#our AI LOL ;-)
                if 'Student/College' in self.offer:
                    self.Student.append(self.offer)
                elif 'Military' in self.offer:
                    self.military.append(self.offer)
                elif 'First Responder' in self.offer:
                    self.First_Responder.append(self.offer)
                elif 'Customer Bonus' in self.offer:
                    self.Customer_Bonus.append(self.offer)
                elif 'Loyalty' in self.offer:
                    self.Loyalty.append(self.offer)
                elif 'Mobility' in self.offer:
                    self.Mobility.append(self.offer)
                elif 'Conquest' in self.offer:
                    self.Conquest.append(self.offer)
                else:
                    pass
            else:
                pass 
        for self.trim_name in response.css('select'):
            yield{
                'Name':response.css('h1.heading-2.mb-1_5::text').extract_first().split()[1],
                'Model':response.css('h1.heading-2.mb-1_5::text').get(),
                'Trim':self.trim_name.css('option::text').get(),
                'Student':self.Student,
                'Military':self.military,
                'First_Responder':self.First_Responder,
                'Bonus':self.Customer_Bonus,
                'Loyalty':self.Loyalty,
                'Conquest':self.Conquest,
                'Mobility':self.Mobility
            }#writing the data
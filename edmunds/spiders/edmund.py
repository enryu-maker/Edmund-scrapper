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
    
    def final_parse(self, response):
        my_dict={
            'Student/College Grad for Retail or Lease':[],
            'Military for Lease':[],
            'First Responder for Retail':[],
            'Lease Bonus Cash':[],
            'Loyalty for Retail or Lease':[],
            'Conquest for Lease':[],
            'Mobility for Retail':[],
            'Loyalty Lender Bonus Cash':[],
            'Student/College Grad Lender Bonus':[],
            'Conquest for Retail':[],
            'Clean Fuel Rebate for Retail or Lease':[],
            'Military for Lease':[],
            'Customer Bonus Cash for Retail or Lease':[],
            'Lender Bonus for Standard APR':[],
            'Student/College Grad for Lease':[],
            'First Responder for Lease':[],
            'Military for Retail':[],
            'First Responder for Retail':[],
            'Limited Term Bonus Cash':[],
            'Employee Pricing':[],
            'Lender':[]}
        self.offers=response.css('li.unordered-list-item')
        self.cash_offers=self.offers.css('span::text').getall()
        value='Customer Bonus Cash for Retail or Lease'
        for offer in self.cash_offers:
            if value in offer :
                    my_dict['Customer Bonus Cash for Retail or Lease'].append(offer)
            else:
                for key in my_dict.keys():
                    if key in offer:
                        my_dict[key].append(offer.split()[0])
        self.details=response.css('p.mb-0::text').getall()
        for self.detail in self.details:
            for key in my_dict.keys():
                if len(my_dict[key])>1 and key.split()[0] in self.detail and key.split()[1] in self.detail:
                        my_dict[key].append(self.detail)

        self.trim_value=response.css('option::text').getall()
        for self.trim_name in self.trim_value:

            yield{
                'Name':response.css('h1.heading-2.mb-1_5::text').extract_first().split()[1],
                'Model':response.css('h1.heading-2.mb-1_5::text').get(),
                'Trim':self.trim_name,
                'Student/College Grad for Retail or Lease':my_dict['Student/College Grad for Retail or Lease'],
                'Military for Retail or Lease':my_dict['Military for Lease'],
                'First Responder for Retail or Lease':my_dict['First Responder for Retail'],
                'Lease Bonus Cash':my_dict['Lease Bonus Cash'],
                'Loyalty for Retail or Lease':my_dict['Loyalty for Retail or Lease'],
                'Conquest for Retail or Lease':my_dict['Conquest for Lease'],
                'Mobility for Retail':my_dict['Mobility for Retail'],
                'Loyalty Lender Bonus Cash':my_dict['Loyalty Lender Bonus Cash'],
                'Student/College Grad Lender Bonus':my_dict['Student/College Grad Lender Bonus'],
                'Conquest for Retail':my_dict['Conquest for Retail'],
                #'Mobility for Retail':my_dict['Mobility for Retail'],
                'Clean Fuel Rebate for Retail or Lease':my_dict['Clean Fuel Rebate for Retail or Lease'],
                'Military for Lease':my_dict['Military for Lease'],
                'Customer Bonus Cash for Retail':my_dict['Customer Bonus Cash for Retail or Lease'],
                'Lender Bonus for Standard APR':my_dict['Lender Bonus for Standard APR'],
                'Student/College Grad for Lease':my_dict['First Responder for Lease'],
                'First Responder for Lease':my_dict['First Responder for Lease'],
                'Military for Retail':my_dict['Military for Retail'],
                'First Responder for Retail':my_dict['First Responder for Retail'],
                'Limited Term Bonus Cash':my_dict['Limited Term Bonus Cash'],
                'Employee Pricing':my_dict['Employee Pricing'],
                'Lender':my_dict['Lender']
                }#writing the data
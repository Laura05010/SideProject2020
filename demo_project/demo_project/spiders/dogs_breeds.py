import sys
import scrapy
import csv

class BreedSpider(scrapy.Spider):
  name = 'dog_breed_scraper'
  #List of URLS to scrape
  start_urls = ['http://www.dogbreedhealth.com/list-of-dog-breeds/']
  
  def parse(self, response):
    # for breed in response.xpath("//div[@class= 'entry-content']/ul/li"):
    # alphabet = yield {'alpha_headings': response.xpath("//div[@class= 'entry-content']/ul/li[@class ='alpha-heading']").extract()}
    
      yield {
        'list': response.xpath("//div[@class= 'entry-content']/ul/li/a").extract()
        }


  #scrapy parse --spider=dog_breed_scraper 'http://www.dogbreedhealth.com/list-of-dog-breeds/'
  # Alphabet = parse(response)
  # print(Alphabet)
  
#GOAL:
#breed_names = {breed:link}


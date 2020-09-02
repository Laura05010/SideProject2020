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

# SCRAPING PER BREED
#LIFESTYLE
# //div[@class= 'lifestyle']/p[2]

#HEALTH & WELFARE PROBLEMS
#Heading
#//div[@class= 'entry-content breed-footer']/p[@class= 'global-heading sub-headed'][2]
#Info 
#//div[@class= 'entry-content breed-footer']/ul[1]


#OTHER DISEASES REPORTED
#Heading
#//div[@class= 'entry-content breed-footer']/p[@class= 'global-heading sub-headed'][4]
#Info
#//div[@class= 'entry-content breed-footer']/ul[2]



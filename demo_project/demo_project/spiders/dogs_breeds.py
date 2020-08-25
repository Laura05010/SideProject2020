import scrapy

class BreedSpider(scrapy.Spider):
  name = 'dog_breed_scraper'
  #List of URLS to scrape
  start_urls = ['http://www.dogbreedhealth.com/list-of-dog-breeds/']
  
  def parse(self, response):
    for breed in response.xpath("//div[@class= 'entry-content']/ul/li"):

      yield {
        'alpha_headings': breed.xpath(".[@class ='alpha-heading']").extract_first()

      }
  
  Alphabet = parse(response)
  print(Alphabet)
  
#POTENTIAL STEPS TO TAKE
    #iterate through A,B,C ..

    #iterate through entire list



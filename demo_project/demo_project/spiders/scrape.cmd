scrapy parse --spider=dog_breed_scraper 'http://www.dogbreedhealth.com/list-of-dog-breeds/'
scrapy parse --spider=info_breed_scraper 'http://www.dogbreedhealth.com/shih-tzu/'

scrapy crawl info_breed_scraper -o info.csv
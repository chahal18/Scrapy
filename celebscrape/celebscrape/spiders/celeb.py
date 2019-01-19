# -*- coding: utf-8 -*-
import scrapy
import re

class CItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    url = scrapy.Field()
    Id = scrapy.Field()
    gender = scrapy.Field()


class CelebSpider(scrapy.Spider):
    name = 'Celeb'
    allowed_domains = ['healthyceleb.com']

    # Mentioning all the urls for the scrapping work.

    start_urls = [
                  'https://healthyceleb.com/category/statistics/sports-stars/female-sports-stars',
                  'https://healthyceleb.com/category/statistics/sports-stars/female-sports-stars/page/2',
                  'https://healthyceleb.com/category/statistics/sports-stars/female-sports-stars/page/3',
                  'https://healthyceleb.com/category/statistics/sports-stars/female-sports-stars/page/4',
                  'https://healthyceleb.com/category/statistics/sports-stars/female-sports-stars/page/5',
                  'https://healthyceleb.com/category/statistics/sports-stars/male-sports-stars',
                  'https://healthyceleb.com/category/statistics/sports-stars/male-sports-stars/page/2',
                  'https://healthyceleb.com/category/statistics/sports-stars/male-sports-stars/page/3',
                  'https://healthyceleb.com/category/statistics/sports-stars/male-sports-stars/page/4',
                  'https://healthyceleb.com/category/statistics/sports-stars/male-sports-stars/page/5'
                 ]

             

    # Defining the parser

    def parse(self, response):

        # Initiating the DmozItem()

        item = CItem()

        #Scrapping the links of player's profile from the start urls

        links = response.xpath('//div[@class="td-block-span6"]//h3[@class="entry-title td-module-title"]')

        for question in links:
            link = question.xpath('a/@href').extract()[0]
            yield scrapy.Request(link, callback = self.parse_attr)   

            # Calling the parse_attr to handle the parsing of the link's data.

            # Scrappy visiting the scrapped links to collect the required data of players.




    def parse_attr(self, response):
        item = CItem()

        # Saving the url of the player's profile in the url. 

        item["url"] = response.url

        # Using try & except block as there are some profile that are having players details in the table format & some have details in the paragraphs.


    # Scrapping the name from the table and then cleaning it by removing the unrequired info. As name is have 'Quick Info'. So removing it. 

        try:            
            cleanName = response.xpath("//div[@class='td-post-content']/table[@class='tablepress tablepress-id-3']/thead/tr[@class='row-1 odd']/th[@class='column-1']/strong/text()").extract()[0]
            cleanName = ' '.join(cleanName.split(' ')[:-2])
# Scrapping the Height from the table.
            cleanHeight = response.xpath("//table[@class='tablepress tablepress-id-3']//tbody//tr[@class='row-2 even']//td[@class='column-2']/text()").extract()[0]
# Scrapping the weight from the table and then removing the 'Kg' unit from it
            cleanWeight = response.xpath("//table[@class='tablepress tablepress-id-3']//tbody//tr[@class='row-3 odd']//td[@class='column-2']/text()").extract()[0]
            cleanWeight = ' '.join(cleanWeight.split(' ')[:-1])  
        except:
            # Now coming to the except block, these new predicates are provided for profiles which are not accessed by above try block.
            cleanName = response.xpath("//div[@class='td-post-content']/p[1]/text()").extract()
            # These height & weight data were being a headache. So created these siblings & ancestors thing to work around it. 
            res = response.xpath("//div[@class='td-post-content']//h3[contains(text(), 'Height')]/following-sibling::p[1]/text()").extract()
            if not res:
                cleanHeight = response.xpath("//strong[text()='Height']/../following-sibling::p[1]/text()").extract()
            else:
                cleanHeight = response.xpath("//div[@class='td-post-content']//h3[contains(text(), 'Height')]/following-sibling::p[1]/text()").extract()
            
            res = response.xpath("//div[@class='td-post-content']//h3[contains(text(), 'Weight')]/following-sibling::p[1]/text()").extract()

            if not res:
                cleanWeight = response.xpath("//strong[text()='Weight']/../following-sibling::p[1]/text()").extract()
            else:
                cleanWeight = response.xpath("//div[@class='td-post-content']//h3[contains(text(), 'Weight')]/following-sibling::p[1]/text()").extract()
    # Saving the scrapped data after processing of the Try-Except block

        item["height"] = cleanHeight

        item["name"] = cleanName        

        item["weight"] = cleanWeight


        # Now for specifying the generator, Using the referer link and using the Try-Except block to check whether the gender is male or female.


        gen = response.request.headers.get('Referer').decode('utf-8')

        try:
            if(re.findall('\\bfemale\\b',gen)[-1] == 'female'):
                item['gender'] = 'Female'
        except:
            item['gender'] = 'Male'

        # Now scrapping the ID from the Url of the player's profile.            
      
        item['Id'] = re.findall('\d+',response.url)[-1]

        yield item
    
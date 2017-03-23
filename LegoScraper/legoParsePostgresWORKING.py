# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from collections import defaultdict
from LegoScraper.items import LegoscraperItem
from scrapy.loader import ItemLoader

class LegoSpider(Spider):
    name = "lego"
    allowed_domains = ["brickset.com"]
    start_urls = ('http://brickset.com/sets/year-2016/page-1/',)

    def parse(self, response):
        sections = response.xpath('.//article[@class="set"]')
        for section in sections:
            #l = ItemLoader(item=LegoscraperItem(), response=response)
            item = LegoscraperItem()
            #row = defaultdict()
            Pieces1 = section.xpath('.//div [@class="col"]/dl[dt="Pieces"]/dd[1]/a/text()').extract_first()
            Pieces2 = section.xpath('.//div [@class="col"]/dl[dt="Pieces"]/dd[1]/text()').extract_first()
            if Pieces1 == None:
                try:
                    item['Pieces'] = int(Pieces2)
                except:
                    item['Pieces'] = Pieces2
                #l.add_value('Pieces',Pieces2)
            else:
                try:
                    item['Pieces'] = int(Pieces1)
                except:
                    item['Pieces'] = Pieces1
                #l.add_value('Pieces',Pieces1)
            #row['Pieces'] = Pieces

            ### this uses the pipelines process_item method to replace None with 'No Pieces'
            # item['Pieces'] = Pieces1
            # item['Pieces'] = Pieces2
            ###
            mfs = section.xpath('.//*[@class="col"]/dl[dt="Minifigs"]/dd[2]/a/text()').extract_first()
            try:
                item["Minifigs"] = int(mfs)
            except:
                item["Minifigs"] = mfs
            #l.add_value('Minifigs',mfs)
            #row['Minifigs'] = mfs
            nts = section.xpath('.//*[@class="col"]/dl[dt="Notes"]/dd[1]/text()').extract_first()
            item['Notes'] = nts
            #l.add_value('Notes',nts)
            #row['Notes'] = nts
            comm = section.xpath('.//*[@class="action"]/dl/dd[1]/text()').extract_first()
            item['Community'] = comm
            #l.add_value('Community',comm)
            #row['Community'] = comm
            #yield row
            yield item
            #yield l.load_item()

        next_page = response.xpath('.//*[@class="pagination"]/ul/li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield Request(next_page)
        # try:
        #     yield Request(next_page)
        # except:
        #     print('END: Site scrapping complete')

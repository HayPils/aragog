# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.com']
    base_url = "https://www.amazon.com/MIU-COLOR-Professional-Deshedding-Effectively/product-reviews/B00DM1DDBW/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls = []

    for i in range(1, 2): 
        start_urls.append(base_url + str(i))

    def parse(self, response):
        data = response.css('#cm_cr-review_list') 
        
        star_rating = data.css('.review-rating')

        comments = data.css('.review-text')
        count = 0

        for review in star_rating:
            yield{
                    'stars': ''.join(review.xpath('.//text()').extract()),
                    'comment': ''.join(comments[count].xpath(".//text()").extract())
                    }
            count=count+1

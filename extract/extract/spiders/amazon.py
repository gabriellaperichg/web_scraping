import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.com.br"]
    start_urls = ["https://www.amazon.com.br/s?i=stripbooks&rh=n%3A6740748011%2Cp_36%3A-2200%2Cp_n_feature_nine_browse-bin%3A8529758011%2Cp_n_condition-type%3A13862762011&dc&qid=1765039756&rnid=13862761011&ref=sr_nr_p_n_condition-type_1&ds=v1%3AzM0bfKZhUGrxmjDqR%2BjeG44Ecn1kvzp4NOZrNlcRAqI"]

    def parse(self, response):
        products = response.css('div.puisg-col-inner')

        for product in products:
            name = product.css('h2.a-size-medium span::text').get()

            if not name:
                continue

            price_text = product.css('span.a-offscreen::text').get()
            price = None

            if price_text:
                price_text = price_text.replace('\xa0', '').replace('R$', '').strip()
                price = float(price_text.replace(',', '.'))

            rate_text = product.css('span.a-size-small.a-color-base::text').get()
            rate = None

            if rate_text:
                rate_text = rate_text.replace(',', '.')
                rate = float(rate_text)

            yield {
                'author': product.xpath('.//span[contains(text(), "por")]/following-sibling::span[1]/text()').get(),
                'name': name.strip(),
                'language': product.xpath('.//span[contains(text(), "Edição")]/text()').get(),
                'rate': rate,
                'price': price
            }

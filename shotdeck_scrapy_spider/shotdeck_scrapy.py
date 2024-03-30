import scrapy
from scrapy.crawler import CrawlerProcess


class DayClass(scrapy.Spider):
    name = "PostcodesSpider"

    custom_settings = {
        'FEED_FORMAT': 'csv',       
        'FEED_URI': 'Extreme%20Wide_urls.csv',
        'CONCURRENT_REQUESTS': '1'
    }

    def start_requests(self):
        yield scrapy.Request(url="https://shotdeck.com/welcome/login", callback=self.parse)

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response, formdata={
            "go": "1",
            "user": "your_login",
            "pass": "your_pass",
            "stay": "1",
        }, callback=self.parse2)

    def parse2(self, response):
        for i in range(0, 300, 30):
            yield scrapy.Request(url="https://shotdeck.com/browse/searchstillsajax/" +
                                     "frame_size/Extreme%20Wide/" + "limit/30/offset/" +
                                     str(i),
                                 callback=self.parse3)

    def parse3(self, response):
        print(response.body)
        imagesData = response.css("div.outerimage")
        for image in imagesData:
            imgURL = "https://shotdeck.com" + image.css(
                "div > div:nth-of-type(1) > a > img::attr(src)").extract_first().replace("smthumb/small_", "")
            vidURL = ""
            if image.css("div > div:nth-of-type(2) > span::attr(class)").extract_first() == "yesclip":
                vidID = imgURL.split("/")
                vidID = vidID[-1]
                vidID = vidID.replace(".jpg", "")
                vidID = vidID.replace(".JPG", "")
                vidID = vidID.replace(".png", "")
                vidID = vidID.replace(".PNG", "")
            yield {
                "Image URL": imgURL,
                "Movie Name": image.css("div > div:nth-of-type(2) > a::text").extract_first()
            }


process = CrawlerProcess()
process.crawl(DayClass)
process.start()
import data_stars.settings as st
import scrapy
from data_stars.utils.net import get_header
from data_stars.utils.os import get_path
from data_stars.utils.time import get_current_time_string
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import (DNSLookupError, TCPTimedOutError,
                                    TimeoutError)

path = get_path(__file__, 3)


class NaverListSpider(scrapy.Spider):
    name = st.NAVER_LIST
    allowed_domains = ['search.shopping.naver.com']
    custom_settings = {'LOG_FILE': f'{path}/logs/{st.NAVER_LIST}/{get_current_time_string()}.log'}

    def __init__(self, name=None, **kwargs):
        super(NaverListSpider, self).__init__(name, **kwargs)
        self.headers = get_header()

    def start_requests(self):
        url = 'https://search.shopping.naver.com/search/all?query={keyword}'

        yield scrapy.Request(
            url=url,
            method='GET',
            headers=self.headers,
            callback=self.parse,
            errback=self.http_error,
            encoding='utf-8',
            meta={'example': 'hello'}
        )

    def parse(self, response, **kwargs):
        print('test :] ', kwargs.get('example'))

        html = response.text
        if not html:
            raise
        for row in response.xpath('//*[@id="content"]/div[1]/div[2]/div/div[1]/div'):
            print(row.get())

    def http_error(self, failure):
        self.logger.info(repr(failure))
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.info('HttpError on %s', response.url)
        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.info('DNSLookupError on %s', request.url)
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.info('TimeoutError on %s', request.url)


class NaverDetailSpider(scrapy.Spider):
    name = st.NAVER_DETAIL

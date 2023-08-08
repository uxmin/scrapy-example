BOT_NAME = "data_stars"

SPIDER_MODULES = ["data_stars.spiders"]
NEWSPIDER_MODULE = "data_stars.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

NAVER_LIST = 'naver_list'

LOG_LEVEL = 'INFO'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

DOWNLOADER_MIDDLEWARES = {'data_stars.middlewares.SaveHtmlMiddleware': 100}

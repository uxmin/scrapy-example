BOT_NAME = "data_stars"

SPIDER_MODULES = ["data_stars.spiders"]
NEWSPIDER_MODULE = "data_stars.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 스파이더명
NAVER_LIST = 'naver_list'
NAVER_DETAIL = 'naver_detail'

# 로그 설정
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
LOG_STDOUT = False
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_FILE_APPEND = True


# HTML문서 저장을 위한 미들웨어
DOWNLOADER_MIDDLEWARES = {
    'data_stars.middlewares.SaveHtmlMiddleware': 100
}

# 크롤링 우회에 필요한 헤더값
USER_AGENT = [
    # 맥북+IE
    ('Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; .NET CLR 2.0.50727;'
     ' .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 3.5.30720; rv:11.0) like Gecko'),
    # 맥북+사파리
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/13.0.5 Safari/605.1.15'),
    # 맥북+파이어폭스
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0',
    # 아이폰+파이어폭스
    ('Mozilla/5.0 (IPhone; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) FxiOS/24.1 '
     'Mobile/15E148 Safari/605.1.15'),
    # 아이폰+사파리
    ('Mozilla/5.0 (Iphone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, likeGecko) Version/13.0.5 '
     'Mobile/15E148 Safari/604.1'),
    # 아이패드+파이어폭스
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/24.1 Safari/605.1.15',
    # 아이패드+사파리
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 '
     'Safari/605.1.15')
]

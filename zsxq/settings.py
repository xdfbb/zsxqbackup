BOT_NAME = 'zsxq'
SPIDER_MODULES = ['zsxq.spiders']
NEWSPIDER_MODULE = 'zsxq.spiders'
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host': 'api.zsxq.com',
    'Origin': 'https://wx.zsxq.com',
    'Referer': 'https://wx.zsxq.com/dweb2/'
}

DOWNLOADER_MIDDLEWARES = {
    'zsxq.middlewares.AuthorizationMiddleware': 543,
    'zsxq.middlewares.ZSXQRetryMiddleware': 544,
    'zsxq.middlewares.ConvertToZsxqApiResponseMiddleware': 545,
    'zsxq.middlewares.HttpHostCheckMiddleware': 546,
}

ITEM_PIPELINES = {
    'zsxq.pipelines.DuplicatesPipeline': 200,
    'zsxq.pipelines.ZsxqPipeline': 300,
    'zsxq.pipelines.GroupItemExportPipeline': 301,
    'zsxq.pipelines.TopicItemExportPipeline': 302,
    'zsxq.pipelines.TopicImagesPipeline': 303,
    'zsxq.pipelines.TopicFilesPipeline': 304,
}

# Web Driver
CHROME_DRIVER_PATH = 'chromedriver'
BACKUP_MODE = 'white'  # or black
DOWNLOAD_MODE = 'incremental'  # or complete

# 备份的圈子id
PICK_GROUP_ID = [
    8424258282, 551151485124, 28512842824421, 1824528822, 4148444128, 454855211158
]

# 不备份的圈子id
IGNORE_GROUP_ID = [
    758548854,  # 帮助与反馈
]

# 授权相关设置
ZSXQ_ACCESS_TOKEN = '6000F9BC-A0CA-8441-A520-9A465B3F08F7_2C999066D114BC4F'
ZSXQ_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

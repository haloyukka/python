import json
from logging.config import dictConfig

with open('logging.json') as f:
    dictConfig(json.load(f))


# 動作確認
from logging import getLogger

# RootLogger: error のみが標準エラーに
root_logger = getLogger()
root_logger.debug('RootLogger: debug')
root_logger.error('RootLogger: error')

# myapp: debug は指定したファイルに
# myapp: error は指定したファイルと標準エラーに
myapp_logger = getLogger('myapp.test')
myapp_logger.debug('myapp: debug')
myapp_logger.error('myapp: error')

# これはすべて無視される
hoge_logger = getLogger('hoge.fuga.piyo')
hoge_logger.debug('hoge: debug')
hoge_logger.error('hoge: error')
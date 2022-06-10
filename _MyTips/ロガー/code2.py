import sys
from logging import getLogger, DEBUG, ERROR, StreamHandler, FileHandler, NullHandler, Formatter
# フォーマッターを定義
simple_formatter = Formatter('%(asctime)s: %(message)s')

# 標準エラー出力に出すためのハンドラを定義
console_handler = StreamHandler(sys.stderr)
console_handler.setLevel(ERROR)
console_handler.setFormatter(simple_formatter)

# 自作アプリ用に全てのログをファイルに書き出すようハンドラを定義
myapp_file_handler = FileHandler('myapp.log')
myapp_file_handler.setLevel(DEBUG)

# ルートロガーにセット
root_logger = getLogger()
root_logger.addHandler(console_handler)

# 自作アプリのパッケージのロガーにセット
myapp_logger = getLogger('myapp')
myapp_logger.setLevel(DEBUG)
myapp_logger.addHandler(myapp_file_handler)

# hoge パッケージのログは全て出さない
hoge_handler = getLogger('hoge')
hoge_handler.addHandler(NullHandler)
hoge_handler.propergate = False
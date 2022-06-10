import sys
from logging import getLogger, DEBUG, StreamHandler

# Setup logger
logger = getLogger(__name__)
logger.setLevel(DEBUG)

handler = StreamHandler(sys.stderr)
handler.setLevel(DEBUG)
logger.addHandler(handler)

def main():
    logger.debug('This is a Debug message')
    logger.info('This is a Info message')
    logger.warning('This is a Warning message')
    logger.error('This is a Error message')
    logger.critical('This is a Critical message')

if __name__ == '__main__':
    main()
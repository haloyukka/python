import configparser

config = configparser.ConfigParser()
config.sections()

config.read('example.ini')
config.sections()

'bitbucket.org' in config
# True

'bytebong.com' in config
# False

config['bitbucket.org']['User']
# hg

config['DEFAULT']['Compression']
# yes

topsecret = config['topsecret.server.com']
topsecret['ForwardX11']

topsecret['Port']

for key in config['bitbucket.org']:
    print(key)


config['bitbucket.org']['ForwardX11']
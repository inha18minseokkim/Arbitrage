import config

class user:
    def __init__(self):
        self.APIKEY = config.get_secret('apiKey')
        self.SECRET = config.get_secret('secret')


if __name__ == '__main__':
    tmp = user()

import os
import configparser
import getpathInfo

path = getpathInfo.get_Path()
config_path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    print('HTTP红的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
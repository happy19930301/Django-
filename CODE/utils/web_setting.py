import json
import os

class WebSetting:
    def __init__(self):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(self.dir, '../../config.json'), 'r') as f:
            self.setting = json.load(f)

    @property
    def DB_NAME(self):
        return self.setting['DB']['name']

    @property
    def DB_USERNAME(self):
        return self.setting['DB']['username']

    @property
    def DB_PASSWORD(self):
        return self.setting['DB']['password']

    @property
    def DB_HOST(self):
        return self.setting['DB']['host']

    @property
    def DB_PORT(self):
        return self.setting['DB']['port']

    @property
    def REDIS_USERNAME(self):
        return self.setting['REDIS']['username']

    @property
    def REDIS_PASSWORD(self):
        return self.setting['REDIS']['password']

    @property
    def REDIS_HOST(self):
        return self.setting['REDIS']['host']

    @property
    def REDIS_PORT(self):
        return self.setting['REDIS']['port']

    @property
    def UPLOAD_FOLDER(self):
        return self.setting['UPLOAD_FOLDER']


own_setting = WebSetting()

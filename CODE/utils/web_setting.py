import json
import os

class WebSetting:
    def __init__(self):
        # 
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


own_setting = WebSetting()

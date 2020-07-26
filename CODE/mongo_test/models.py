from mongoengine import Document
from mongoengine import (StringField, LongField, BooleanField, DynamicField)

class Finance(Document):
    is_invested = BooleanField(help_text='是否投资')
    number = StringField(help_text='股票，基金代码')
    name = StringField(help_text='股票，基金名字')
    company = StringField(help_text='公司名字（如管理基金的公司）')
    create_time = LongField(help_text='创建的时间戳')


class User(Document):
    name = StringField()
    pages = StringField()
    time = LongField()
    descirption = DynamicField()

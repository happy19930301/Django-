from django.db import models
from django.contrib.auth.models import User

# class DailyTestJob(models.Model):

#     name = models.CharField(max_length=32)
#     test_time = models.DateTimeField()
#     status = models.CharField(max_length=16)

#     class Meta:
#         abstract = True
#         app_label = 'job'


# class DailyTestJob(models.Model):

#     name = models.CharField(max_length=32)
#     test_time = models.DateTimeField()
#     status = models.CharField(max_length=16)

#     class Meta:
#         app_label = 'job'  # 建的表名为 job_dailytestjob

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__
        attrs['add'] = lambda self, value: self.append(value)
        return super_new(cls, name, bases, attrs, **kwargs)


class MyList(list, metaclass=ListMetaClass):
    def sub(self):
        self.remove()
    pass


def run():
    # user = User.objects.get(pk=1)
    user = User.objects.filter(pk__gt=0).values('username', 'id').order_by('-id')
    print(user)
    # li = MyList()
    # li.add(2)
    # print(li)

from django.db import models

# Create your models here.
'''
1、需要继承自models.Model，基类，增删改查等
2、系统自动添加主键ID
3、字段：
    字段名 = model.类型(选项)
    字段名不要用关键字，class def 等
'''
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
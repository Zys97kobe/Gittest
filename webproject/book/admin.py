from django.contrib import admin
from book.models import Book
from book.models import PeopleInfo
'''
注册模型，注册表，把model里得创建的类在这里进行注册，放到数据库中。
'''
admin.site.register(Book)
admin.site.register(PeopleInfo)
# Register your models here.

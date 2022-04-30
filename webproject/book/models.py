from django.db import models

# Create your models here.
'''
1、需要继承自models.Model，基类，增删改查等
2、系统自动添加主键ID
3、字段：
    字段名 = model.类型(选项)
    字段名不要用关键字，class def 等
    不要用连续的下划线
4、类型：
    CharField
    BooleanField
    AutoField
    DateField
5、限制条件：
    lenth
    是否唯一 unique
    是否为空 null  blank
6、修改表名称
    
'''
class Book(models.Model):
    name = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=100)
    pub_date = models.DateField(null=True)
    readcount = models.BigIntegerField(default=0)
    commentcount = models.BigIntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'Bookinfo'
        verbose_name = '书籍管理'

    def __str__(self):
        #显示书籍名字
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
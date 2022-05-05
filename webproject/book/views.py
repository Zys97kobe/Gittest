from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book

'''
view 函数
1、接受请求
2、返回响应 HttpResponse
'''
# Create your views here.
def index(request):
    books = Book.objects.all()
    print(books)
    return HttpResponse('index')

'''**************增加***************'''
# 方式一
book = Book(
    name='Django',
    author='IDK',
    pub_date = '2000-1-1',
    readcount = 10
)

# 方式二
# objects 可以实现增删改查
Book.objects.create(
    name = '测试开发入门',
    author = 'IDK',
    pub_date = '2020-1-1',
    readcount = 52,
)

'''**************修改***************'''
# 方式一
book6 = Book.objects.get(id = 6)
book6.name = '运维开发'
book6.save()

# 方式二
Book.objects.filter(id=5).update(name = '测试开发',
                                 commentcount = 1200,)

'''**************删除***************'''
# 方式一

book6 = Book.objects.get(id =6 )
book6.delete()

# 方式二

Book.objects.filter(id=5).delete()

'''**************查询***************'''

#查询编号为1的图书
Book.objects.get(id=1)#get得到一个对象
Book.objects.get(id__exact=1)
Book.objects.get(pk=1)#Primary Key主键
Book.objects.filter(id=1)#得到一个列表

# 查询书名包含‘湖’
Book.objects.get(name__contains='湖')
Book.objects.filter(name__contains='湖')

# 查询书名以'部'结尾
Book.objects.filter(name__endswith='部')

# 查询书名为空的图书
Book.objects.filter(name__isnull=True)

# 查询编号为1，3，5的图书
# select * from book where id in (1,3,5)
Book.objects.filter(id__in=[1,3,5])
Book.objects.filter(id__in=(1,3,5))

# 查询编号大于3 的图书
# 于 gt 小于 lt 大于等于gte 小于等于 lte
Book.objects.filter(id__gt=3)

# 查询编号不等于3的图书
Book.objects.exclude(id=3)

# 查询1980年发表的图书
Book.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
Book.objects.filter(pub_date__gt='1990-1-1')

# F对象
# 进行两个属性比较
from django.db.models import F
# 查询阅读量大于等于评论量的图书
Book.objects.filter(readcount__gt=F('commentcount'))

# Q对象
# 与语法，并且查询
# 查询阅读量大于20，并且编号小于3的图书
Book.objects.filter(readcount__gt=20).filter(id__lt=3)
Book.objects.filter(readcount__gt=20,id__lt=3)

# 或语法，或者查询
from django.db.models import Q
# 查询阅读量大于20，或者编号小于3的图书
Book.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

Book.objects.filter(Q(readcount__gt=20)&Q(id__lt=3))

# 非语法，not
Book.objects.filter(~Q(id=3))

# 聚合函数
# Sum Max Min Avg Count
# 语法：类名.objects.aggregate(聚合函数("字段名"))
from django.db.models import Sum,Max,Min,Avg,Count
Book.objects.aggregate(Sum('readcount'))

# 排序
# SQL语句：select * from table order by "字段" 默认升序，
# select * from table order by "字段" desc为降序
# 升序
Book.objects.all().order_by("readcount")
# 降序
Book.objects.all().order_by("-readcount")


'''**************级联查询***************'''
# 关联查询
# 查询书籍为1的所有人物信息
# 获取id为1的书籍：
# 【一对多】的关系模型中，在‘一’的模型中，
# 系统自动添加一个 [关联模型类名]_set 以及 [关联模型类名] （隐藏添加）

book= Book.objects.get(id=1)
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
from book.models import PeopleInfo
people = PeopleInfo.objects.get(id=1)
people.book

# 关联过滤查询
# 语法：
    #模型类名.objects.filter(关联模型类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为郭靖
Book.objects.filter(peopleinfo__name__exact='郭靖')

# 查询图书，要求图书中人物的描述包含”八“
Book.objects.filter(peopleinfo__description__contains='八')

# 查询书名为”天龙八部“的所有人物
PeopleInfo.objects.filter(book__name__exact = '天龙八部')


# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt = 30)

'''**************查询结果集***************'''
# QuerySet
# all() fiter() exclude() order_by()
# 两大特性：
# 惰性执行：不用不查询
book = Book.objects.all()
# 此时没有进行SQL查询
Book.objects.all()
# 此时进行SQL查询


# 缓存
# 列表推导式

[book.id for book in Book.objects.all()]
[book.id for book in Book.objects.all()]
# 执行几次就需要查询几次


books= Book.objects.all()
[book.id for book in books]
# 不管执行几次 都只需要查询一次 因为有缓存


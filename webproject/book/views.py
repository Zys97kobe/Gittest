from django.shortcuts import render
from django.http import HttpResponse
'''
view 函数
1、接受请求
2、返回响应 HttpResponse
'''
# Create your views here.
def index(request):


    return HttpResponse("VIEW函数，返回HttpResponse")
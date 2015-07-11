#coding:utf-8
# from django.http import HttpResponse
from django.shortcuts import render
 
# def index(request):
#     return HttpResponse(u"欢迎光临 自强学堂!")


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

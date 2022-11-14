from django.http import HttpResponse;
from django.shortcuts import render
# from mysite import templates
# from mysite import a
def index(request):
    return HttpResponse('welcome to django predator rock it main')
def predator(request):
    params={'name':'Aamir','age':24,'place':'delhi'}
    return render(request,'index.html',params)
    #  return HttpResponse("hello james")
def about(request):
    return HttpResponse("about predator <a href='/'>back</a>")

def home(request):
    return HttpResponse('welcome to home page aamir my wrapping extension is very good and it is very good for the development ')
def markup(request):
    #in this way we can load the html for the dev
    # return HttpResponse('<h1>hello heading of html</h1>')"
    return HttpResponse('<a href="https://www.leetcode.com/"target="_blank">Visit W3Schools.com!</a>')
def pre(request):
    return HttpResponse('hello buddy django')
from django.http import HttpResponse;
from django.shortcuts import render
import string
# from mysite import templates
# from mysite import a
def index(request):
    return HttpResponse('welcome to django predator rock it main')
def predator(request):
    # params={'name':'Aamir','age':24,'place':'delhi'}
    return render(request,'index.html')
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
# def capi(request):
#     # print(request.GET.get('text','default'))
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse('text area analysis')
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    if(removepunc=='on'):
        puntuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        # print(puntuations)
        analyzed=""
        for it in djtext:
            if it not in puntuations:
                analyzed+=it
        params={'purpose':'to remove punctuation',
                 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
        # return HttpResponse('hello')
    else:
        return HttpResponse('error please on the button')


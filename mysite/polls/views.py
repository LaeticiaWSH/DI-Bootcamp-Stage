from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Titi(request):
    return HttpResponse("Hi! Good morning to you.")

def product(request):
    return render(request,"product.html",{})

def About(request):
    return HttpResponse('<h1> Welcome Users<h1>')

def blogarticle(request,articleid):
    article = Blog.objects.get(id=articleid)
#     articles =[
#         {
#             'title' : 'My first time trying django',
#             'body' : 'Today is the 10th of August'
#         },
#         {
#             'title' : 'Python is actually a snake .',
#             'body' :'While you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python's Flying Circus. One of the amazing features of Python is the fact that it is actually one person's work.'
#         }
#     ]
    return render(request,"blogarticle.html",{'title': article.title,'body': article.body})

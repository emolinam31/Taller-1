from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return HttpResponse("<h1>Welcome To The Home Page<h1>")
   return render(request, "home.html",  {'name':'Greg Lim'})

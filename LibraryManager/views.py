from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hey, you made it. This is the secret page. Go <a href='/admin'>here</a>.")
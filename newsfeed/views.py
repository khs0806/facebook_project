from django.shortcuts import render

# Create your views here.

def newsfeed(request):
    return render(request, 'newsfeed/newsfeed.html')
from django.shortcuts import render
from news.models import News


# Create your views here.
def home(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})

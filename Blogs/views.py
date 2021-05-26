from django.shortcuts import render
from Blogs.models import Post
# Create your views here.
def home(request):
    articles = Post.objects.all()
    return render(request, 'home.html', {'articles': articles})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-created_date')
	return render(request, "blog/listBlog.html", {
		'posts' : posts
		})

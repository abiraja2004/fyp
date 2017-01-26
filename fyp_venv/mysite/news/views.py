from datetime import datetime
from django.shortcuts import render
from .models import Post

# Create your views here.
def hello_world(request):
	return render (request, 'hello_world.html',{
		'current_time': str(datetime.now()),
	})

def home(request):
	post_list=Post.objects.all()
	return render (request, 'home.html',{
		'post_list': post_list,
	})
	
def politics(request):
	post_list=Post.objects.all()
	return render (request, 'politics.html',{
		'post_list': post_list,
	})

def finance(request):
	post_list=Post.objects.all()
	return render (request, 'finance.html',{
		'post_list': post_list,
	})
	
def post_detail(request, pk):
	post=Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post': post})
from datetime import datetime
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create views 
def hello_world(request):
	return render (request, 'hello_world.html',{
		'current_time': str(datetime.now()),
	})

# create home page
def home(request):
	post_list=Post.objects.all()
	return render (request, 'home.html',{
		'post_list': post_list,
	})

#create politics 
def politics(request):
	post_list = Post.objects.all().filter(category="politics").order_by('pub_date').reverse()
	paginator = Paginator(post_list, 9)  # create a paginator

	page = request.GET.get('page')  # get the page number
	try:
		post_list = paginator.page(page)  # get the corresponding page
	except PageNotAnInteger:
		post_list = paginator.page(1)  
	except EmptyPage:  
		post_list = paginator.page(paginator.num_pages)  

	return render (request, 'politics.html',{
		'post_list': post_list,
	})

# create finance
def finance(request):
	post_list = Post.objects.all().filter(category="finance").order_by('pub_date').reverse()
	paginator = Paginator(post_list, 9) 

	page = request.GET.get('page')  
	try:
		post_list = paginator.page(page)  
	except PageNotAnInteger:  
		post_list = paginator.page(1)  
	except EmptyPage:  
		post_list = paginator.page(paginator.num_pages)  

	return render (request, 'finance.html',{
		'post_list': post_list,
	})

# create news page
def post_detail(request, pk):
	post=Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post': post})

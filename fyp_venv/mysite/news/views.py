from datetime import datetime
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

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
	post_list = Post.objects.all().filter(category="politics").order_by('pub_date').reverse()
	paginator = Paginator(post_list, 9)  # 实例化一个分页对象

	page = request.GET.get('page')  # 获取页码
	try:
		post_list = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		post_list = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		post_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

	return render (request, 'politics.html',{
		'post_list': post_list,
	})
	
def finance(request):
	post_list = Post.objects.all().filter(category="finance").order_by('pub_date').reverse()
	paginator = Paginator(post_list, 9)  # 实例化一个分页对象

	page = request.GET.get('page')  # 获取页码
	try:
		post_list = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		post_list = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		post_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

	return render (request, 'finance.html',{
		'post_list': post_list,
	})
	
# def politics(request):
	# post_list=Post.objects.all()
	# return render (request, 'politics.html',{
		# 'post_list': post_list,
	# })

# def finance(request):
	# post_list=Post.objects.all()
	# return render (request, 'finance.html',{
		# 'post_list': post_list,
	# })
	
def post_detail(request, pk):
	post=Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post': post})
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from news.models import Post
from news.models import Quotation
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean

# 接收POST请求数据
def search_post(request):
	ctx ={}
	SearchQuerySet()
	try:
		sqs = SearchQuerySet().filter(content=AutoQuery(request.POST['q']))
	except KeyError:
		sqs = 'False'
	if request.POST:
		ctx['rlt'] = sqs
	return render(request, "opinion_post.html", ctx)
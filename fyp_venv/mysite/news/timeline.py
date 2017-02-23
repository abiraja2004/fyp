# -*- coding: utf-8 -*-
import sys
from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib import messages
from news.models import Post
from news.models import Quotation
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean

from TimeLine import headlineExtraction

# receive POST request data
def search_post(request):
    ctx ={}
    SearchQuerySet()
    try:
        sqs = SearchQuerySet().filter(content=AutoQuery(request.POST['q'])).order_by('pub_date')
        ## Pass the summarizer and read the list
        result = headlineExtraction.getSummarizedList(sqs)

        ## Check headlineExtraction results
        #sys.stdout = sys.__stdout__
        #for i in result:
        #    print(i)
        
        messages.info(request,result)
        
        sqs = SearchQuerySet().filter(title__in=result).order_by('pub_date')
        
    except KeyError:
        sqs = 'False'
    if request.POST:
        ctx['rlt'] = sqs
    return render(request, "timeline.html", ctx)


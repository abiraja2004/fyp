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

#   receive POST request data in backend server
def search_post(request):
    ctx ={}
    SearchQuerySet()
    try:
        #   Search all revelent news to user input keywords
        sqs = SearchQuerySet().filter(content=AutoQuery(request.POST['q'])).order_by('pub_date')
        # Pass the summarizer and read the list
        result = headlineExtraction.getSummarizedList(sqs)   
        messages.info(request,result)
        
        #   Sorted by pub_date
        sqs = SearchQuerySet().filter(title__in=result).order_by('pub_date')
        
    except KeyError:
        sqs = 'False'
    if request.POST:
        ctx['rlt'] = sqs

    #   Pass the POST array to frontend, the html template
    return render(request, "timeline.html", ctx)


from django.http import HttpResponse
from django.shortcuts import render_to_response

# form
def search_form(request):
	return render_to_response('search_form.html')

# receive request data
def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		message = request.GET['q']
	else:
		message = 'No Result'
	return HttpResponse(message)

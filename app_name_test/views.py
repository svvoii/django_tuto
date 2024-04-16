# Here the http `request` is handled and the http `response` is returned.  
# This file also can be called as `request_handler.py'

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
	return render(request, 'hello.html', { 'name': 'Serge' })
	# return HttpResponse('Hello, World!')

from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.http import Http404
# Create your views here.
def login(request):
	if request.METHOD == 'post':
		return HttpResponse('login')
	return render_to_response("blog/login.html")

@login_required(login_url='blog_login')
def home(request):
	return render_to_response("blog/home.html")

def test(request):
	raise Http404("I am 404")
	return render_to_response('blog/jquery_test.html')

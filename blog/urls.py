from django.conf.urls import url, include
from django.contrib.auth import views as authViews
import views

urlpatterns = [
				url(r'^$', views.home, name = 'blog_home'),
				url(r'^login/$', authViews.login, {'template_name':'blog/login.html'}, name='blog_login'),	
				url(r'^test/$', views.test, name='blog_jquery_test')
			]
from django.conf.urls import url, include
from django.contrib.auth import views as authViews
import views

urlpatterns = [
				url('^$', views.home, name = 'blog_home'),
				url('^login/', authViews.login, {'template_name':'blog/login.html'}, name='blog_login'),	
			]
from django.conf.urls import url, include
import views

urlpatterns = [
               url(r'^$', views.home, name='polls_home'),
               url(r'^detail/(?P<question_id>[0-9]{1,2})/$', views.detail, name='detail'),
               url(r'^results/(?P<question_id>[0-9]{1,2})/$', views.results, name='results'),
               url(r'^vote/(?P<question_id>[0-9]{1,2})/$', views.vote, name='vote'),
               ]
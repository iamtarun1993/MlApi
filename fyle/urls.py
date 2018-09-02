from django.conf.urls import url
from fyle import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^branch_details/(?P<branch_ifsc>\w+)$', views.branch_details, name='branch_details'),
    url(r'^bank_list/(?P<bank_name>.*)/(?P<bank_city>.*)$', views.bank_list, name='bank_list'),
    url(r'^omdb/(?P<id>.*)$', views.omdb, name='omdb')
]
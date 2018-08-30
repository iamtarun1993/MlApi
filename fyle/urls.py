from django.conf.urls import url
from fyle import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^branch_details/(?P<branch_ifsc>\w+)$', views.branch_details, name='branch_details'),
    url(r'^bank_list/(?P<bank_name>.*)/(?P<bank_city>.*)$', views.bank_list, name='bank_list'),
    #url(r'^v1/(?P<variable_a>(\d+))/(?P<variable_b>(\d+))/$', r'custom1.views.v1')
]
from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Zerodha$', views.zerodha_index, name='zerodha_index'),
    url(r'^Test$', views.test, name='test'),
    url(r'^zerodha_main$', views.zerodha_main, name='zerodha_main'),
    url(r'^csv_data_top$', views.csv_data_top, name='csv_data_top'),
    url(r'^csv_data_bottom$', views.csv_data_bottom, name='csv_data_bottom'),
    url(r'^csv_data_all$', views.csv_data_all, name='csv_data_all'),
    url(r'^Stock/(?P<stock_id>\d+)$', views.stock_index, name='stock_index'),
    url(r'^stock_info/(?P<stock_id>\d+)$', views.stock_info, name='stock_info'),
]

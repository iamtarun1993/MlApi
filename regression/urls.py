from django.conf.urls import url
from regression import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linear_regression$', views.linear_regression, name='linear_regression'),
]
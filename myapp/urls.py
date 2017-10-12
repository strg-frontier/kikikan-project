from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.myapp_index,name='myapp_index'),
    url(r'^delete$',views.myapp_delete,name='myapp_delete'),
]


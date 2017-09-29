from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.helloworld_index,name='helloworld_index'),

]

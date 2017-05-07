from django.conf.urls import url
from . import views

app_name="appoint"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^task/(?P<id>\d+)$', views.task, name='task'),
    url(r'^delete/(?P<rev_id>\d+)$', views.delete, name='delete'),
    url(r'^update_task$', views.update_task, name="update_task"),

]

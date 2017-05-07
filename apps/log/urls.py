from django.conf.urls import url
from . import views

app_name = "log"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reg$', views.reg, name='reg'),
    url(r'^login$', views.login, name='login'),
    url(r'^user_info/(?P<id>\d+)$', views.user_info, name='user_info'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^delete_user$', views.delete_user, name='delete_user'),
    url(r'^update_user$', views.update_user, name='update_user'),
    url(r'^start_reg$', views.start_reg, name='start_reg'),
    url(r'^start_log$', views.start_log, name='start_log'),

]

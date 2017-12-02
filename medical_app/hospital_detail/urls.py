from django.conf.urls import url

from hospital_detail import views

app_name = 'hospital_detail'

urlpatterns = [
    url(r'^list/$', views.hospital_list, name='list'),
    url(r'^list/(?P<pk>[0-9]+)/detail/$', views.hospital_detail,
        name='detail')

]

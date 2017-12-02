from django.conf.urls import url
from hospital_detail import views

app_name = 'hospital_detail'

urlpatterns = [
    url(r'^details/$', views.hospitalDetail, name='detail')
]

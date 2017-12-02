from django.conf.urls import url

from register_hospital import views

app_name = 'register_hospital'

urlpatterns = [
    url(r'^login/$', views.login, name='register'),
    url(r'^sign-up/$', views.signUp, name='sign-up')
]

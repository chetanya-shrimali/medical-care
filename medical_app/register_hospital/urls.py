from django.conf.urls import url

from register_hospital import views

app_name = 'register_hospital'

urlpatterns = [
    url(r'^login/$', views.user_login, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^sign-up/$', views.SignUpFormView.as_view(), name='signup'),
    url(r'^(?P<pk>[0-9]+)/validate/$', views.validate, name='validate'),
]

from django.conf.urls import url
from userapp import views

app_name = 'userapp'

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.register, name='register'),
    url(r'^loggedout/',views.after_logout,name='afterlogout')
]

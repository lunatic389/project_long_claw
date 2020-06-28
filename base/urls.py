from django.urls import path
from . import views

app_name='base'


urlpatterns = [
    path('homepage/',views.index,name='home'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('search/',views.search,name='search'),
    path('requests/',views.requests,name='request')

]

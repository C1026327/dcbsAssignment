from django.urls import path
from . import views


app_name = 'itregistration'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('about', views.about, name='contact'),
    path('modules', views.modules, name='modules'),

]
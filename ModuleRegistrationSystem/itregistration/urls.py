from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CourseListView

app_name = 'itregistration'
urlpatterns = [

    path('', CourseListView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contact', views.about, name='contact'),
    path('modules', PostListView.as_view(), name='modules'),
    path('modules/<int:pk>', PostDetailView.as_view(), name='modules_detail'),
    path('modules/new', PostCreateView.as_view(), name='modules_create'),
    path('modules/<int:pk>/update', PostUpdateView.as_view(), name='modules_update'),
    path('modules/<int:pk>/delete',PostDeleteView.as_view(), name='modules_delete'),
    path('issue/<str:username>', UserPostListView.as_view(), name='user_modules'),
]
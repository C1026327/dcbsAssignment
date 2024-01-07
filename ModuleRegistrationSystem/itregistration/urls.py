from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CourseListView, ContactFormView, ModuleRegistration, modulewithdrawl

app_name = 'itregistration'
urlpatterns = [

    path('', CourseListView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('modules', PostListView.as_view(), name='modules'),
    path('modules/<int:pk>', PostDetailView.as_view(), name='modules_detail'),
    path('modules/new', PostCreateView.as_view(), name='modules_create'),
    path('modules/<int:pk>/update', PostUpdateView.as_view(), name='modules_update'),
    path('modules/<int:pk>/delete',PostDeleteView.as_view(), name='modules_delete'),
    path('modules/<str:username>', UserPostListView.as_view(), name='user_modules'),
    path('modules/<int:pk>/registration', ModuleRegistration, name='moduleregistration'),
    path('modules/<int:pk>/resignation', modulewithdrawl.as_view(), name='resignation')
]
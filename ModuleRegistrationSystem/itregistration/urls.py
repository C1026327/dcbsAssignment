from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'itregistration'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('about', views.about, name='contact'),
    path('modules', PostListView.as_view(), name='modules'),
    path('modules/<int:pk>', PostDetailView.as_view(), name='module_detail'),
    path('modules/new', PostCreateView.as_view(), name='module-create'),
    path('modules/<int:pk>/update', PostUpdateView.as_view(), name='module-update'),
    path('modules/<int:pk>/delete',PostDeleteView.as_view(), name='modules-delete'),
]
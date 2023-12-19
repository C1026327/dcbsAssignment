from django.shortcuts import render, get_object_or_404
from .models import Module, Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import View


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper
# Create your views here.

def about(request):
    return render(request, 'itregistration/about.html', {'title':'About Us'})

def contact(request):
    return render(request, 'itregistration/contact.html', {'title':'Contact Us'})

def modules(request):
    module = {'modules':Module.objects.all(), 'title': 'Modules'}
    return render(request, 'itregistration/modules.html', module)

class PostListView(ListView):
    model = Module
    template_name = 'itregistration/modules.html'
    context_object_name = 'modules'
    ordering = ['-date_submitted']
    paginate_by = 3

class CourseListView(ListView):
    model = Course
    template_name = 'itregistration/home.html'
    paginate_by = 3
    context_object_name = 'courses'

class UserPostListView(ListView):
    model = Module
    template_name = 'itregistration/user_modules.html'
    context_object_name = 'modules'
    paginate_by = 3

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Module.objects.filter(author=user).order_by('-date_submitted')

class PostDetailView(DetailView):
    model = Module

@superuser_required()

class PostCreateView(CreateView):
    model = Module
    fields = ['modulename', 'category', 'credit', 'description']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Module
    fields = ['category', 'credit', 'description']

    def test_func(self):
        module = self.get_object()
        return self.request.user == module.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Module
    success_url = '/modules'
    def test_func(self):
        module = self.get_object()
        return self.request.user == module.author

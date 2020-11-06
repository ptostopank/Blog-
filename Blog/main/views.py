from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView 
from .forms import ArticleForm, LoginUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'articles'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'main/article.html'
    context_object_name = 'get_article'

class ArticleEditView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Article
    template_name = 'main/editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')
    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Article.objects.all()
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'main/editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user_id:
            return self.handle_no_permission()
        return kwargs

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'main/editpage.html'
    success_url = reverse_lazy('editpage')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.user_id:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class UserLoginView(LoginView):
    template_name = 'main/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('editpage')
    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('editpage')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('editpage')
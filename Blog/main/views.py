from django.http import request
from django.shortcuts import render
from .models import User, Article
from django.views.generic import ListView
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    template = 'main/index.html'
    context = {
        'articles': articles,
    }
    return render(request, template, context)

def article_detail(request, id):
    get_article = Article.objects.get(id=id)
    template = 'main/article.html'
    context = {
        'get_article': get_article,
    }
    return render(request, template, context)

def edit_page(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()


    articles = Article.objects.all()
    template = 'main/editpage.html'
    context = {
        'list_articles': articles,
        'form': ArticleForm(),
    }
    return render(request, template, context)




def sign_in(request):
    return render(request, 'main/signin.html')


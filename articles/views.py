from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from articles.models import Article


# class IndexView(TemplateView):
#     template_name = 'articles/index.html'
def index(request):
    articles = Article.objects
    return render(request, 'articles/index.html', {'articles':articles})

def article_list(request):
    articles = Article.objects
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, article_id):
    detail_article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article_detail.html', {'article':detail_article})
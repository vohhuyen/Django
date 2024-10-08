from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.db import transaction
from django.db.models import Count

def article_list(request):
    recent_articles = Article.objects.recent() 
    return render(request, 'articles/article_list.html', {'articles': recent_articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_create(request):
    if request.method == "POST":
        article = Article(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.POST['author']
        )
        article.save()
        return redirect('article_list')
    return render(request, 'articles/article_form.html')

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.author = request.POST['author']
        article.save()
        return redirect('article_detail', pk=article.pk)
    return render(request, 'articles/article_form.html', {'article': article})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

def article_list_view(request):
    articles = Article.objects.all()
    count = Article.objects.aggregate(total=Count('id'))['total']
    return render(request, 'articles/article_list.html', {'articles': articles, 'article_count': count})

def search_articles_view(request):
    query = request.GET.get('q') 
    if query:
        articles = Article.objects.filter(title__icontains=query) 
    else:
        articles = Article.objects.all() 
    return render(request, 'articles/search_results.html', {'articles': articles, 'query': query})
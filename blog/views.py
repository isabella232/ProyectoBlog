from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
#importamos para paginación
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def list(request):

    #sacar artículos
    articles = Article.objects.all()

    #Painar los artículos
    paginator = Paginator(articles, 2) #indicamos la lista de articulos que quiero pagina , y le indico el número de articulo que queremos por página

    #recoger número página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos', #indicando el titulo de la página que se muestra en el html list.html entre corchetes
        'articles': page_articles
    })

@login_required(login_url='login')
def category(request, category_id):
    
    # category = Category.objects.get(id = category_id) 
    category = get_object_or_404(Category, id=category_id) #Aquí lo que  lo que hacemos es que cuando no existe el id de una categoria que pasamos por la url, mostremos un error 404
    #articles = Article.objects.filter(categories=category_id)

    return render(request, 'categories/category.html', {
        "category": category
        # 'articles': articles
    })

@login_required(login_url='login')
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })
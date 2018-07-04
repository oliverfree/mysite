from django.shortcuts import render, get_object_or_404, render_to_response
from .models import BlogArticles
# Create your views here.


def homepage(request):
    response = render_to_response("home.html")
    return response


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status = 'Published', category = category_id)
    category = get_object_or_404(Category, pk = category_id)
    context = {
        'posts' : posts,
        'category' : category,
    }

    return render (request, 'posts_by_category.html', context)
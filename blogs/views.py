from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status = 'Published', category = category_id)
    category = get_object_or_404(Category, pk = category_id) # we can also use try/except when we want to do some custom action if the category does not exists

    context = {
        'posts' : posts,
        'category' : category,
    }

    return render (request, 'posts_by_category.html', context)

def blogs(request, slug): 
    single_blog = get_object_or_404(Blog, slug=slug, status = 'Published')
    context = {
        'single_blog' : single_blog,
    }
    return render(request, 'blogs.html' , context)
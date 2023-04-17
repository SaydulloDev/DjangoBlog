from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category, Tag


# Create your views here.
class HomePage(ListView):
    queryset = Post.objects.all()
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# New Post List View for Order by Created Date
class NewPosts(ListView):
    queryset = Post.objects.order_by('-created_at')
    template_name = 'blog/new_posts.html'
    context_object_name = 'posts'


# Categories List View for All
class CategoriesView(ListView):
    queryset = Category.objects.all()
    template_name = 'blog/categories.html'
    context_object_name = 'categories'

    def get_object(self, queryset=None):
        return Category.objects.get(slug=self.kwargs['slug'])


# Categories Detail view
class CategoriesDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(category_id=self.object)
        context['posts'] = posts
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


def base_template(request):
    tags = Tag.objects.all()
    category = Category.objects.all()
    post = Post.objects.order_by('-created_at')
    context = {'tags': tags, 'category': category, 'post': post}
    return render(request, 'base.html', context)

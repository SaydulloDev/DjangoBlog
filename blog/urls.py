from django.urls import path

from .views import HomePage, CategoriesView, NewPosts, CategoriesDetailView, PostDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),  # Home page
    path('new_posts/', NewPosts.as_view(), name='new_posts'),  # New Posts List View
    path('categories/', CategoriesView.as_view(), name='categories'),  # Category List View
    path('categories/<slug:slug>/', CategoriesDetailView.as_view(),
         name='categories_detail'),  # Category Detail View
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),  # Post Detail View
]

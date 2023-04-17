from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
from .author import Author
from .category import Category
from .tag import Tag


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True, null=False, verbose_name='Slug')
    content = models.TextField()
    image = models.ImageField(verbose_name='Image')
    video = EmbedVideoField(verbose_name='Video Link')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name='#Tags')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

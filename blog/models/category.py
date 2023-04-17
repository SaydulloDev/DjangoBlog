from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    image = models.ImageField(null=False)
    slug = models.SlugField(unique=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

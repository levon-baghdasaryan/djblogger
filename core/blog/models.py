from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post_author')
    status = models.CharField(max_length=10, choices=options, default='draft')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('post_single', args=[self.slug])

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

import factory
from django.contrib.auth import get_user_model

from core.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    password = 'test'
    username = 'test'
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'x'
    subtitle = 'x'
    slug = 'x'
    author = factory.SubFactory(UserFactory)
    content = 'x'
    status = 'published'

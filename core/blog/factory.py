import factory
from django.contrib.auth import get_user_model
from factory.faker import faker

from .models import Post

User = get_user_model()
FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=5)
    subtitle = factory.Faker('sentence', nb_words=8)
    slug = factory.Faker('slug')
    author = User.objects.get_or_create(username='admin')[0]

    @factory.lazy_attribute
    def content(self):
        x = ''
        for _ in range(5):
            x += '\n' + FAKE.paragraph(nb_sentences=30) + '\n'
        return x

    status = 'published'

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add(
                "Python",
                "Django",
                "Database",
                "Pytest",
                "JavaScript",
                "VSCode",
                "Deployment",
                "Full-Stack",
                "ORM",
                "Front-End",
                "Back-End"
            )

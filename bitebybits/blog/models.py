from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """
    Custom manager for retrieving all post with
    status 'published'.
    """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('trashed', 'Trashed')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')

    objects = models.Manager()  # default manager
    publish = PublishedManager()  # custom manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

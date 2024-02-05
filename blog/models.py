from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class PublishManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # status choices
    class Status(models.TextChoices):
        DRAFT = "DF", "DRAFT"
        PUBLISHED = "PB", "PUBLISHED"
        REJECTED = "RJ", "REJECTED"

    # relational data
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_posts')

    # data fields
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishManager

    # show title in admin panel

    def __str__(self):
        return self.title
    #

    class Meta:
        ordering = ('-publish', '-updated')
        indexes = [models.Index(fields=['-publish', '-updated'])]

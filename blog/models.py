from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse

# Create your models here.
# jalali calender is used


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
        User, on_delete=models.CASCADE, related_name='user_posts', verbose_name="کاربر")

    # data fields
    title = models.CharField(max_length=255, verbose_name="تیتر")
    description = models.TextField(verbose_name="متن")
    slug = models.SlugField(unique=True, verbose_name="لینک")
    publish = jmodels.jDateTimeField(
        default=timezone.now, verbose_name="انتشار")
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name="ساخت")
    updated = jmodels.jDateTimeField(auto_now=True, verbose_name="به روز شده")
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="وضعیت")

    objects = jmodels.jManager()
    published = PublishManager

    # show title in admin panel

    def __str__(self):
        return self.title
    #

    class Meta:
        ordering = ('-publish', '-updated')
        indexes = [models.Index(fields=['-publish', '-updated'])]
        verbose_name = "پست "
        verbose_name_plural = "  پست ها"

    def get_absulote_url(self, *args, **kwargs):
        return reverse('blog:detail', args=[self.id])

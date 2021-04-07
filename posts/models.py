from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import TextField
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField("Название поста", max_length = 50)
    text = RichTextField("Текст поста")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pubdate = models.DateTimeField("Время создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
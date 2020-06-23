from django.contrib import admin

# Register your models here.
from article import models
from .models import ArticleColumn


# 注册ArticlePost到admin中
admin.site.register(models.ArticlePost)
# 注册文章栏目
admin.site.register(ArticleColumn)
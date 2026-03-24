from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name',]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','created_at','author',]
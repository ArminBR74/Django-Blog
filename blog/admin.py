from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'publish', 'status')
    ordering = ['publish',]
    list_filter = ['user', 'status']
    search_fields = ('title',)
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['status']

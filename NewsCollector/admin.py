from django.contrib import admin
from .models import HackerNewsArticles

# Register your models here.
class HackerNewsArticlesAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'article_name', 'article_comment_count', 'article_posted_on', 'article_upvotes']
    list_filter = ['article_posted_on', 'article_name']


admin.site.register(HackerNewsArticles, HackerNewsArticlesAdmin)
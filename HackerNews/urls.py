from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HackerNews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    url(r'^$', 'HackerNews.views.homepage_view', name='home'),
    url(r'^login/', 'HackerNews.views.login_view', name='login'),
    url(r'^register/', 'HackerNews.views.register_view', name="resgister"),
    url(r'^logout/', 'HackerNews.views.logout_view', name="resgister"),
    url(r'^markarticle/', 'UserNews.views.mark_article_read_or_delete_view', name="markarticle"),
    url(r'^getarticles/', 'HackerNews.views.get_articles_view', name="getarticles"),
)

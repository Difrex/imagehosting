# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^new$', views.image_new, name='image_new'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.image_detail, name='image_detail'),
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_post, name='delete_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', login, {'template_name':'imagehosting/login.html'}, name='login'),
    url(r'^logout/$', logout)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

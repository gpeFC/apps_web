# Fichero URL :: Project: newBlog

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(
    r'^post/(?P<idpost>[0-9]+)/$',
    'poster.views.one_post',
    name="one_post",
  ),
  url(
    r'^category/(?P<idcategory>[0-9]+)/$'
    'poster.views.posts_by_category',
    name="post_by_category",
  ),
  url(
    r'^$',
    'poster.views.home',
    name="home",
  ),
)

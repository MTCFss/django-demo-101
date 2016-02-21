from django.conf.urls import url
from .views import contact, post_list, post_detail, author_detail, author_list

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<post_id>\d+)$', post_detail, name='post_detail'),
    url(r'^author$', author_list, name='author_list'),
    url(r'^author/(?P<author_id>\d+)$', author_detail, name='author_detail'),
    url(r'^contact$', contact, name='contact'),

]
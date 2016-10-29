from django.conf.urls import url
from .views import contact, PostList, PostDetail, AuthorDetail, AuthorList

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/?$', PostDetail.as_view(), name='post_detail'),
    url(r'^author/?$', AuthorList.as_view(), name='author_list'),
    url(r'^author/(?P<pk>\d+)/?$',
        AuthorDetail.as_view(), name='author_detail'),
    url(r'^contact/?$', contact, name='contact'),

]

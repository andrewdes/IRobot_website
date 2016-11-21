from django.conf.urls import url

from website import views

urlpatterns = [
    url(r'^index/$', views.index, name='website_index'),
    url(r'^forward/$', views.forward, name='website_forward'),
    url(r'^back/$', views.back, name='website_back'),
    url(r'^left/$', views.left, name='website_left'),
    url(r'^right/$', views.right, name='website_right'),
    url(r'^topRight/$', views.forward, name='website_topright'),
    url(r'^topLeft/$', views.back, name='website_topleft'),
    url(r'^bottomRight/$', views.left, name='website_bottomright'),
    url(r'^bottomLeft/$', views.right, name='website_bottomleft'),

]
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'scanqr$', views.escaneo, name='escaneo'),
    url(r'cliente$', views.reg_cliente , name='cliente'),
    url(r'menu$', views.menu, name='menu'),
    url(r'cocina$', views.cocina, name='cocina'),


)

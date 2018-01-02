from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'scanqr$', views.escaneo, name='escaneo'),
    url(r'prueba$', views.prueba, name='test'),

)
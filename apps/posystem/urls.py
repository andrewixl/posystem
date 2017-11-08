from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^request$', views.request),
    url(r'^request/add$', views.addrequest),
    url(r'^vote$', views.vote),
    url(r'^export$', views.export),
    url(r'^status$', views.status),
    url(r'^vote/(?P<product_id>\d+)$', views.voteProduct),
    url(r'^status/(?P<product_id>\d+)$', views.editstatus),
    url(r'^changestatus/(?P<product_id>\d+)$', views.changestatus),
    url(r'^addvendor$', views.addVendor),
    url(r'^createvendor$', views.createVendor),
]

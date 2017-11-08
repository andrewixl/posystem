from . import views
from django.conf.urls import url
def test(request):
	print 'in app'

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
	url(r'^createclub$', views.createclub),
	url(r'^addclub$', views.addclub),
	url(r'^$', views.index),
]

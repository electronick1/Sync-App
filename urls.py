from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^integration/add/$', views.add_integration, name='add_integration'),
    url(r'^integration/(?P<integration_id>\d+)/edit/$', views.edit_integration, name='edit_integration'),
    url(r'^integration/(?P<integration_id>\d+)/delete/$', views.delete_integration, name='delete_integration'),
]

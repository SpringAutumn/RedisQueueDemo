from django.conf.urls import patterns, include, url
from rest_framework import routers
from fresh import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task.views.home', name='home'),
    # url(r'^task/', include('task.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

router = routers.DefaultRouter()
router.register(r'fresh', views.FreshViewSet)
urlpatterns += router.urls

urlpatterns += patterns('', (r'^admin/django-rq/', include('django_rq.urls')),)
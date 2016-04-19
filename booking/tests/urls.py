"""URLs to run the tests."""
try:
    from django.conf.urls import include, url
except ImportError:  # Pre-Django 1.4 version
    from django.conf.urls.defaults import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^booking/', include('booking.urls')),
]

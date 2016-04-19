"""URLs for the booking app."""
try:
    from django.conf.urls import url
except ImportError:  # Pre-Django 1.4 version
    from django.conf.urls.defaults import url

from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/$',
        views.BookingDetailView.as_view(),
        name='booking_detail'),
    url(r'^create/$',
        views.BookingCreateView.as_view(),
        name='booking_create'),
    url(r'^$', views.BookingListView.as_view(), name='booking_list'),
]

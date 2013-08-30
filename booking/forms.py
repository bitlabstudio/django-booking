"""Forms for the ``booking`` app."""
from django import forms
from django.conf import settings

from .models import Booking, BookingStatus


class BookingForm(forms.ModelForm):
    def __init__(self, session=None, user=None, *args, **kwargs):
        self.user = user
        self.session = session
        super(BookingForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.instance.pk:
            self.instance.user = self.user
            self.instance.session = self.session
            status_object, created = BookingStatus.objects.get_or_create(
                slug=getattr(settings, 'BOOKING_STATUS_CREATED', 'pending'))
            self.instance.booking_status = status_object
        return super(BookingForm, self).save(*args, **kwargs)

    class Meta:
        model = Booking
        fields = ('gender', 'title', 'forename', 'surname', 'nationality',
                  'street1', 'street2', 'city', 'zip_code', 'country', 'phone',
                  'special_request', 'date_from', 'date_until')

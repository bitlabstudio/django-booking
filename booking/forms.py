"""Forms for the ``booking`` app."""
from django import forms
from django.conf import settings

from .models import Booking, BookingStatus


class BookingForm(forms.ModelForm):
    def __init__(self, session=None, user=None, *args, **kwargs):
        self.user = user
        self.session = session
        super(BookingForm, self).__init__(*args, **kwargs)
        # fields that should remain blank / not required
        keep_blank = [
            'phone', 'notes', 'street2', 'title', 'user', 'session',
            'date_from', 'date_until', 'special_request', 'time_period',
            'time_unit']
        # set all fields except the keep_blank ones to be required, since they
        # need to be blank=True on the model itself to allow creating Booking
        # instances without data
        for name, field in self.fields.iteritems():
            if name not in keep_blank:
                self.fields[name].required = True

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

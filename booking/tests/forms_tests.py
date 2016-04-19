"""Form tests for the ``booking`` app."""
from django.test import TestCase

from mixer.backend.django import mixer

from ..forms import BookingForm
from ..models import Booking


class BookingFormTestCase(TestCase):
    longMessage = True

    def setUp(self):
        self.status = mixer.blend('booking.BookingStatus')

    def test_form(self):
        form = BookingForm()
        self.assertTrue(form, msg=('Form has been initiated.'))

        data = {
            'gender': 'mr',
            'forename': 'Foo',
            'nationality': 'DE',
            'street1': 'Foostreet 12',
            'city': 'Foocity',
            'zip_code': 'ABC123',
            'country': 'DE',
        }
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid(), msg=('Form should be invalid.'))

        data.update({'surname': 'Bar'})
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid(), msg=('Form should be valid.'))

        form.save()
        self.assertEqual(Booking.objects.count(), 1, msg=(
            'One booking should have been created.'))
        self.assertEqual(
            Booking.objects.all()[0].booking_status.slug,
            'pending', msg=('Slug of status should be pending.'))

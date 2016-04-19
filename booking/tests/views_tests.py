"""View tests for the ``booking`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import views
from ..models import Booking


class BookingCreateViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.BookingCreateView

    def setUp(self):
        self.user = mixer.blend('auth.User')

    def test_view(self):
        self.is_callable(add_session=True)

        data = {
            'gender': 'mr',
            'forename': 'Foo',
            'surname': 'Bar',
            'nationality': 'DE',
            'street1': 'Foostreet 12',
            'city': 'Foocity',
            'zip_code': 'ABC123',
            'country': 'DE',
        }
        self.is_postable(data=data, add_session=True,
                         to_url_name='booking_detail')
        self.assertEqual(Booking.objects.count(), 1, msg=(
            'One booking should have been created.'))
        self.assertTrue(Booking.objects.all()[0].session.session_key, msg=(
            'Booking should have a session key.'))
        self.is_postable(data=data, add_session=True,
                         to_url_name='booking_detail')
        self.assertEqual(Booking.objects.count(), 2, msg=(
            'Another booking should have been created.'))

        self.is_postable(data=data, user=self.user, add_session=True,
                         to_url_name='booking_detail')
        self.assertEqual(self.user.bookings.count(), 1, msg=(
            'User should have a new booking.'))
        self.assertTrue(Booking.objects.all()[0].user.username, msg=(
            'Booking should have a user.'))


class BookingDetailViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.BookingDetailView

    def setUp(self):
        self.user = mixer.blend('auth.User')
        self.booking = mixer.blend('booking.Booking')

    def get_view_kwargs(self):
        return {'pk': self.booking.pk}

    def test_view(self):
        self.is_not_callable()
        self.is_not_callable(user=self.user)
        self.booking = mixer.blend('booking.Booking', user=self.user)
        self.is_callable(user=self.user)


class BookingListViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.BookingListView

    def setUp(self):
        self.user = mixer.blend('auth.User')
        mixer.blend('booking.Booking', user=self.user)

    def test_view(self):
        self.is_callable(user=self.user)

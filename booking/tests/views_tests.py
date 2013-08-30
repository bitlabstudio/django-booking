"""View tests for the ``booking`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from .factories import BookingFactory
from ..models import Booking


class BookingCreateViewTestCase(ViewTestMixin, TestCase):
    def setUp(self):
        self.user = UserFactory()

    def get_view_name(self):
        return 'booking_create'

    def test_view(self):
        self.is_callable()

        data = {
            'gender': 'male',
            'forename': 'Foo',
            'surname': 'Bar',
            'nationality': 'DE',
            'street1': 'Foostreet 12',
            'city': 'Foocity',
            'zip_code': 'ABC123',
            'country': 'DE',
        }
        self.is_callable(method='post', data=data)
        self.assertEqual(Booking.objects.count(), 1, msg=(
            'One booking should have been created.'))
        self.assertTrue(Booking.objects.all()[0].session.session_key, msg=(
            'Booking should have a session key.'))
        self.is_callable(method='post', data=data)
        self.assertEqual(Booking.objects.count(), 2, msg=(
            'Another booking should have been created.'))

        self.is_callable(method='post', data=data, user=self.user)
        self.assertEqual(Booking.objects.count(), 1, msg=(
            'There should be no bookings left, after the related session has'
            ' been destroyed.'))
        self.assertEqual(self.user.bookings.count(), 1, msg=(
            'User should have a new booking.'))
        self.assertTrue(Booking.objects.all()[0].user.username, msg=(
            'Booking should have a user.'))


class BookingDetailViewTestCase(ViewTestMixin, TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.booking = BookingFactory()

    def get_view_name(self):
        return 'booking_detail'

    def get_view_kwargs(self):
        return {'pk': self.booking.pk}

    def test_view(self):
        self.is_not_callable()
        self.is_not_callable(user=self.user)
        self.booking = BookingFactory(user=self.user)
        self.is_callable(user=self.user)


class BookingListViewTestCase(ViewTestMixin, TestCase):
    def setUp(self):
        self.user = UserFactory()
        BookingFactory(user=self.user)

    def get_view_name(self):
        return 'booking_list'

    def test_view(self):
        self.is_not_callable()
        self.is_callable(user=self.user)

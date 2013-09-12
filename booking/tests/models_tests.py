"""Tests for the models of the booking app."""
from django.test import TestCase

from . import factories


class BookingTestCase(TestCase):
    longMessage = True

    def setUp(self):
        self.booking = factories.BookingFactory()

    def test_instance(self):
        self.assertTrue(self.booking.pk, msg=(
            'Booking model should have been created.'))


class BookingItemTestCase(TestCase):
    longMessage = True

    def setUp(self):
        self.booking_item = factories.BookingItemFactory()

    def test_instance(self):
        self.assertTrue(self.booking_item.pk, msg=(
            'Booking item model should have been created.'))


class BookingErrorTestCase(TestCase):
    """Tests for the ``BookingError`` model class."""
    longMessage = True

    def test_instantiation(self):
        bookingerror = factories.BookingErrorFactory()
        self.assertTrue(bookingerror.pk)


class BookingStatusTestCase(TestCase):
    longMessage = True

    def setUp(self):
        self.booking_status = factories.BookingStatusFactory()

    def test_instance(self):
        self.assertTrue(self.booking_status.pk, msg=(
            'Booking status model should have been created.'))


class ExtraPersonInfoTestCase(TestCase):
    longMessage = True

    def setUp(self):
        self.info = factories.ExtraPersonInfoFactory()

    def test_instance(self):
        self.assertTrue(self.info.pk, msg=(
            'Person info model should have been created.'))

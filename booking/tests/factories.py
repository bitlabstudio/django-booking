"""Factories for the booking app."""
import factory

from django_libs.tests.factories import UserFactory
from django_libs.tests.factories import SimpleTranslationMixin

from .. import models


class BookingStatusFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for the ``BookingStatus`` model."""
    FACTORY_FOR = models.BookingStatus

    slug = factory.Sequence(lambda x: 'status-{}'.format(x))

    @staticmethod
    def _get_translation_factory_and_field():
        return (BookingStatusTranslationFactory, 'status')


class BookingStatusTranslationFactory(factory.Factory):
    """Factory for ``BookingStatusTranslation`` objects."""
    FACTORY_FOR = models.BookingStatusTranslation

    name = factory.Sequence(lambda x: 'Status {}'.format(x))
    status = factory.SubFactory(BookingStatusFactory)
    language = 'en'


class BookingFactory(factory.DjangoModelFactory):
    """Factory for the ``Booking`` model."""
    FACTORY_FOR = models.Booking

    forename = 'Foo'
    surname = 'Bar'
    booking_status = factory.SubFactory(BookingStatusFactory)


class BookingItemFactory(factory.DjangoModelFactory):
    """Factory for the ``BookingItem`` model."""
    FACTORY_FOR = models.BookingItem

    booking = factory.SubFactory(BookingFactory)
    booked_item = factory.SubFactory(UserFactory)


class ExtraPersonInfoFactory(factory.DjangoModelFactory):
    """Factory for the ``ExtraPersonInfo`` model."""
    FACTORY_FOR = models.ExtraPersonInfo

    booking = factory.SubFactory(BookingFactory)
    forename = 'Foo'
    surname = 'Bar'

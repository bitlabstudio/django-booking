"""Models for the ``booking`` app."""
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_libs.models_mixins import SimpleTranslationMixin
from international.models import countries


class BookingStatus(SimpleTranslationMixin, models.Model):
    """
    Master data containing all booking status.
    For translatable fields check ``BookingStatusTranslation``.

    :slug: A unique slug identifier.

    """
    slug = models.SlugField(
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.slug


class BookingStatusTranslation(models.Model):
    """
    Translatable fields of the ``BookingStatus`` model.

    :name: The name of the status.

    Needed by simple translation:
    :language: The language of the translation.
    :status: The status this translation belongs to.

    """
    name = models.CharField(
        max_length=128,
        verbose_name=_('Name'),
    )

    # needed by simple translation
    language = models.CharField(max_length=16)
    status = models.ForeignKey(BookingStatus)

    def __unicode__(self):
        return self.name


class Booking(models.Model):
    """
    Model to contain information about a booking.

    :user (optional): Connection to Django's User model.
    :session (optional): Stored session to identify anonymous users.
    :gender: Gender of the user.
    :title (optional): Title of the user.
    :forename: First name of the user.
    :surname: Last name of the user.
    :nationality: The nationality of the user.
    :street1: Street address of the user.
    :street2: Additional street address of the user.
    :city: City of the user's address.
    :zip_code: ZIP of the user's address.
    :country: Country of the user's address.
    :phone: Phone number of the user.
    :special_request (optional): A special request of the customer.
    :date_from (optional): From when the booking is active.
    :date_until (optional): Until when the booking is active.
    :creation_date: Date of the booking.
    :booking_id (optional): Custom unique booking identifier.
    :booking_status: Current status of the booking.
    :notes (optional): Staff notes.

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        related_name='bookings',
        blank=True, null=True,
    )

    session = models.ForeignKey(
        'sessions.Session',
        verbose_name=_('Session'),
        blank=True, null=True,
    )

    gender = models.CharField(
        max_length=10,
        verbose_name=_('Gender'),
        choices=(
            ('female', _('female')),
            ('male', _('male')),
        ),
        blank=True,
    )

    title = models.CharField(
        max_length=10,
        verbose_name=_('Title'),
        choices=(
            ('dr', _('Dr.')),
            ('prof', _('Prof.')),
        ),
        blank=True,
    )

    forename = models.CharField(
        verbose_name=_('First name'),
        max_length=20,
        blank=True,
    )

    surname = models.CharField(
        verbose_name=_('Last name'),
        max_length=20,
        blank=True,
    )

    nationality = models.CharField(
        max_length=2,
        verbose_name=_('Nationality'),
        choices=countries,
        blank=True,
    )

    street1 = models.CharField(
        verbose_name=_('Street 1'),
        max_length=256,
        blank=True,
    )

    street2 = models.CharField(
        verbose_name=_('Street 2'),
        max_length=256,
        blank=True,
    )

    city = models.CharField(
        verbose_name=_('City'),
        max_length=256,
        blank=True,
    )

    zip_code = models.CharField(
        verbose_name=_('ZIP/Postal code'),
        max_length=256,
        blank=True,
    )

    country = models.CharField(
        max_length=2,
        verbose_name=_('Country'),
        choices=countries,
        blank=True,
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
    )

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=256,
        blank=True,
    )

    special_request = models.TextField(
        max_length=1024,
        verbose_name=_('Special request'),
        blank=True,
    )

    date_from = models.DateTimeField(
        verbose_name=_('From'),
        blank=True, null=True,
    )

    date_until = models.DateTimeField(
        verbose_name=_('Until'),
        blank=True, null=True,
    )

    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
    )

    booking_id = models.CharField(
        max_length=100,
        verbose_name=_('Booking ID'),
        blank=True,
    )

    booking_status = models.ForeignKey(
        'booking.BookingStatus',
        verbose_name=('Notes'),
        blank=True,
    )

    notes = models.TextField(
        max_length=1024,
        verbose_name=('Notes'),
        blank=True,
    )

    class Meta:
        ordering = ['-creation_date']

    def __unicode__(self):
        return '#{} ({})'.format(self.booking_id or self.pk,
                                 self.creation_date)


class BookingItem(models.Model):
    """
    Model to connect a booking with a related object.

    :quantity: Quantity of booked items.
    :persons (optional): Quantity of persons, who are involved in this booking.
    :booked_item: Connection to related booked item.
    :booking: Connection to related booking.

    """
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Quantity'),
    )

    persons = models.PositiveIntegerField(
        verbose_name=_('Persons'),
        blank=True, null=True,
    )

    # GFK 'booked_item'
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    booked_item = generic.GenericForeignKey('content_type', 'object_id')

    booking = models.ForeignKey(
        'booking.Booking',
        verbose_name=_('Booking'),
    )

    class Meta:
        ordering = ['-booking__creation_date']

    def __unicode__(self):
        return '{} ({})'.format(self.booking, self.booked_item)


class ExtraPersonInfo(models.Model):
    """
    Model to add extra information of persons/guests to a booking.

    :forename: First name of the user.
    :surname: Last name of the user.
    :arrival: Arrival date of the guest.
    :booking: Connection to related booking.
    :message: An additional message regarding this person.

    """
    forename = models.CharField(
        verbose_name=_('First name'),
        max_length=20,
    )

    surname = models.CharField(
        verbose_name=_('Last name'),
        max_length=20,
    )

    arrival = models.DateTimeField(
        verbose_name=_('Arrival'),
        blank=True, null=True,
    )

    booking = models.ForeignKey(
        'booking.Booking',
        verbose_name=_('Booking'),
    )

    message = models.TextField(
        max_length=1024,
        verbose_name=_('Message'),
        blank=True,
    )

    class Meta:
        ordering = ['-booking__creation_date']

    def __unicode__(self):
        return '{} {} ({})'.format(self.forename, self.surename, self.booking)

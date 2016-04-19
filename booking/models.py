"""Models for the ``booking`` app."""
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django_libs.models_mixins import TranslationModelMixin
from django_countries.fields import CountryField
from hvad.models import TranslatableModel, TranslatedFields


class BookingStatus(TranslationModelMixin, TranslatableModel):
    """
    Master data containing all booking status.
    For translatable fields check ``BookingStatusTranslation``.

    :slug: A unique slug identifier.

    translated:
    :name: The displayable name for the status.

    """
    slug = models.SlugField(
        verbose_name=_('Slug'),
    )

    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_('Name'),
            max_length=128,
        )
    )


@python_2_unicode_compatible
class Booking(models.Model):
    """
    Model to contain information about a booking.

    Note, that on the model itself, most of the attributes are blank=True.
    We need this behaviour to be able to create empty temporary bookings.
    You will have to take care of the field being required or not in a
    ModelForm yourself.

    :user (optional): Connection to Django's User model.
    :session (optional): Stored session to identify anonymous users.
    :gender (optional): Gender of the user.
    :title (optional): Title of the user.
    :forename (optional): First name of the user.
    :surname (optional): Last name of the user.
    :nationality (optional): The nationality of the user.
    :street1 (optional): Street address of the user.
    :street2 (optional): Additional street address of the user.
    :city (optional): City of the user's address.
    :zip_code (optional): ZIP of the user's address.
    :country (optional): Country of the user's address.
    :phone (optional): Phone number of the user.
    :email: Email of the user.
    :special_request (optional): A special request of the customer.
    :date_from (optional): From when the booking is active.
    :date_until (optional): Until when the booking is active.
    :time_period (optional): How long the period from date_from will be.
      e.g.: 10 (days).
    :time_unit (optional): What unit of time the period is of. e.g. nights or
      days.
    :creation_date: Date of the booking.
    :booking_id (optional): Custom unique booking identifier.
    :booking_status: Current status of the booking.
    :notes (optional): Staff notes.
    :total (optional): Field for storing a total of all items.
    :currency (optional): If total is uses, we usually also need a currency.

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
            ('mrs', _('Mrs')),
            ('mr', _('Mr')),
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

    nationality = CountryField(
        max_length=2,
        verbose_name=_('Nationality'),
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

    country = CountryField(
        max_length=2,
        verbose_name=_('Country'),
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
        verbose_name=('Booking status'),
        blank=True, null=True,
    )

    notes = models.TextField(
        max_length=1024,
        verbose_name=('Notes'),
        blank=True,
    )

    time_period = models.PositiveIntegerField(
        verbose_name=_('Time period'),
        blank=True, null=True,
    )

    time_unit = models.CharField(
        verbose_name=_('Time unit'),
        default=getattr(settings, 'BOOKING_TIME_INTERVAL', ''),
        max_length=64,
        blank=True,
    )

    total = models.DecimalField(
        max_digits=36,
        decimal_places=2,
        verbose_name=_('Total'),
        blank=True, null=True,
    )

    currency = models.CharField(
        verbose_name=_('Currency'),
        max_length=128,
        blank=True,
    )

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return '#{} ({})'.format(self.booking_id or self.pk,
                                 self.creation_date)


@python_2_unicode_compatible
class BookingError(models.Model):
    """
    Holds information about an error during a booking process.

    This can be particularly useful, when many of the processes are automated
    or reliant on a third party app or API. You then can store the returned
    values directly into this model and have easy access and reference to the
    actual booking.

    :booking: The booking during this error occurred.
    :message: The short error message, that you need to store.
    :details: A more in depth text about the error or any kind of additional
      information, e.g. a traceback.
    :date: The time and date this error occured.

    """
    booking = models.ForeignKey(
        Booking,
        verbose_name=_('Booking'),
    )
    message = models.CharField(
        verbose_name=_('Message'),
        max_length=1000,
        blank=True,
    )
    details = models.TextField(
        verbose_name=_('Details'),
        max_length=4000,
        blank=True,
    )

    date = models.DateTimeField(
        verbose_name=_('Date'),
        auto_now_add=True,
    )

    def __str__(self):
        return u'[{0}] {1} - {2}'.format(self.date, self.booking.booking_id,
                                         self.message)


@python_2_unicode_compatible
class BookingItem(models.Model):
    """
    Model to connect a booking with a related object.

    :quantity: Quantity of booked items.
    :persons (optional): Quantity of persons, who are involved in this booking.
    :subtotal (optional): Field for storing the price of each individual item.
    :booked_item: Connection to related booked item.
    :booking: Connection to related booking.

    properties:
    :price: Returns the full price for subtotal * quantity.

    """
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Quantity'),
    )

    persons = models.PositiveIntegerField(
        verbose_name=_('Persons'),
        blank=True, null=True,
    )

    subtotal = models.DecimalField(
        max_digits=36,
        decimal_places=2,
        verbose_name=_('Subtotal'),
        blank=True, null=True,
    )

    # GFK 'booked_item'
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    booked_item = GenericForeignKey('content_type', 'object_id')

    booking = models.ForeignKey(
        'booking.Booking',
        verbose_name=_('Booking'),
    )

    class Meta:
        ordering = ['-booking__creation_date']

    def __str__(self):
        return u'{} ({})'.format(self.booking, self.booked_item)

    @property
    def price(self):
        return self.quantity * self.subtotal


@python_2_unicode_compatible
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

    def __str__(self):
        return u'{} {} ({})'.format(self.forename, self.surname, self.booking)

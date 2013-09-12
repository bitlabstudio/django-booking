"""Utils for the booking app."""
from django.contrib.sessions.models import Session

from .models import Booking


def get_booking(request):
    """
    Returns the booking that is in progress for the current user or None

    We assume that a user can only have one booking that is in-progress.

    TODO: This implementation assumes that there is a status called
    'inprogress' and that there should only be one such booking for a given
    user. We need to see if this can be more generic for future projects.

    :param request: The Request object.

    """
    booking = None
    if request.user.is_authenticated():
        try:
            booking = Booking.objects.get(
                user=request.user,
                booking_status__slug='inprogress')
        except Booking.DoesNotExist:
            # The user does not have any open bookings
            pass
    else:
        session = Session.objects.get(
            session_key=request.session.session_key)
        try:
            booking = Booking.objects.get(session=session)
        except Booking.DoesNotExist:
            # The user does not have any bookings in his session
            pass
    return booking


def persist_booking(booking, user):
    """
    Ties an in-progress booking from a session to a user when the user logs in.

    If we don't do this, the booking will be lost, because on a login, the
    old session will be deleted and a new one will be created. Since the
    booking has a FK to the session, it would be deleted as well when the user
    logs in.

    We assume that a user can only have one booking that is in-progress.
    Therefore we will delete any existing in-progress bookings of this user
    before tying the one from the session to the user.

    TODO: Find a more generic solution for this, as this assumes that there is
    a status called inprogress and that a user can only have one such booking.

    :param booking: The booking that should be tied to the user.
    :user: The user the booking should be tied to.

    """
    if booking is not None:
        existing_bookings = Booking.objects.filter(
            user=user, booking_status__slug='inprogress').exclude(
            pk=booking.pk)
        existing_bookings.delete()

        booking.session = None
        booking.user = user
        booking.save()

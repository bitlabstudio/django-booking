"""Registering translated models for the ``booking`` app."""
from simple_translation.translation_pool import translation_pool

from .models import BookingStatus, BookingStatusTranslation


translation_pool.register_translation(BookingStatus, BookingStatusTranslation)

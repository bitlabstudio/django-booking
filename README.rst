Django Booking
==============

A reusable Django app that manages bookings for various purposes.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-booking

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/bitmazk/django-booking.git#egg=booking

TODO: Describe further installation steps (edit / remove the examples below):

Add ``booking`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'booking',
    )

Add the ``booking`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^booking/', include('booking.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate booking


Usage
-----

If you allow anonymous bookings, the session object is stored within the
booking model. Otherwise it will be connected to the User model.

NOTE: If a session is destroyed, the connected booking model will also be
removed.

In order to allow login via email and booking ID, please add this to your
``AUTHENTICATION_BACKENDS``::

    AUTHENTICATION_BACKENDS = (
        # your usual auth backends
        'booking.auth_backends.BookingIDBackend',
    )

At the moment you will have to write a new view that will render the
``booking.forms.BookingIDAuthenticationForm``. If the form is valid, your
view should call ``auth_login(request, form.get_user())``, similar to Django's
original login view.

Settings
--------

BOOKING_STATUS_CREATED
++++++++++++++++++++++

Default: 'pending'

Slug of the ``BookingStatus``, which should be added after booking creation.

BOOKING_TIME_INTERVAL
+++++++++++++++++++++

Default: ''

The default value for the ``time_unit`` attribute of the Booking. Set it in
case you need to specify that you want to book something e.g. X days or Y
hours. Set it to the singular of that time unit:::

   BOOKING_TIME_INTERVAL = 'day'


Error logging
+++++++++++++

In case you want to add error logging especially for booking processes, we
provide a ``BookingError`` model, in which you can store:

+-------------+--------------------------------------------------------------------------+
| ``booking`` | (FK to Booking - required) The booking during this error occurred.       |
+-------------+--------------------------------------------------------------------------+
| ``message`` | (Char) The short error message, that you need to store.                  |
+-------------+--------------------------------------------------------------------------+
| ``details`` | (Text) A more in depth text about the error or any kind of additional    |
|             | information, e.g. a traceback.                                           |
+-------------+--------------------------------------------------------------------------+


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-booking
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.

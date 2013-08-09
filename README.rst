Django Booking
============

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

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-booking
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch

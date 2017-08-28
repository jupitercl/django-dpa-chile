Django Political-Administrative Division of Chile
=================================================

``Regiones - Provincias - Comunas``
===================================

Information obtained from the api of Modernization and Digital Government Unit

https://apis.digital.gob.cl/dpa

Pypi
====

https://pypi.python.org/pypi/django-dpa-chile

IMPORT REMOVE OLD VERSION <= 2.0.5
==================================

Force remove foreign key

    DROP TABLES django_dpa_region
    DROP TABLES django_dpa_provincia
    DROP TABLES django_dpa_comuna

Installation
------------

install **django-dpa-chile** using **pip**


    pip install django-dpa-chile

add **dpa_chile** to **INSTALLED_APPS**

settings.py
-----------

    # ...

    INSTALLED_APPS =[
    ...
    'dpa_chile',
    ]

    # ...

Populate
--------

    python manage.py migrate django_dpa_chile

    python manage.py populate_dpa_chile

Use
---

    from django_dpa_chile.models import Region, Provincia, Comuna

Django Political-Administrative Division of Chile
=================================================

``Regiones - Provincias - Comunas``
===================================

Information obtained from the api of Modernization and Digital Government Unit

https://apis.digital.gob.cl/dpa

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

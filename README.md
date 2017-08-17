# django-dpa-chile
###Political-Administrative Division of Chile
### Regiones - Provincias - Comunas
Information obtained from the api of Modernization and Digital Government Unit
https://apis.digital.gob.cl/dpa

## Installation

install `django-dpa-chile` using `pip`

```sh
pip install -U django-dpa-chile
```

add `django_dpa_chile` to INSTALLED_APPS

__settings.py__

```python
# ...

INSTALLED_APPS =[
  ...
  'django_dpa_chile'
  ]

# ...
```

## Populate

```sh
python manage.py populate_dpa_chile
```

## Use

```python
from django_dpa_chile.models import Region, Provincia, Comuna
```
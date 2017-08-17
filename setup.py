#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-dpa-chile',
    version='0.2.1',
    url='https://github.com/jupitercl/django-dpa-chile',
    author='Francisco Jordan',
    author_email='franciscojordan@live.com',
    description=('Political-Administrative Division of Chile'),
    long_description=open('README.md').read(),
    keywords='django,chile,comunas,regiones,provincias',
    license=open('LICENSE').read(),
    platforms=['Mac'],
    packages=[
        'django_dpa_chile',
        'django_dpa_chile.migrations',
        'django_dpa_chile.management',
        'django_dpa_chile.management.commands'],
    include_package_data=True,
    install_requires=[
        'django>=1.11',
        'urllib3',
        'bunch'
    ],
    extras_require={},
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Other/Nonlisted Topic'],
)

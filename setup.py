
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = ''

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = ''

setup(
    name='django-dpa-chile',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.7b1',

    description='Political-Administrative Division of Chile',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/jupitercl/django-dpa-chile',

    # Author details
    author='Francisco Jordan',
    author_email='franciscojordan@live.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
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
    ],

    # What does your project relate to?
    keywords='django chile comunas regiones provincias',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[
        'django_dpa_chile',
        'django_dpa_chile.migrations',
        'django_dpa_chile.management',
        'django_dpa_chile.management.commands'],

    include_package_data=True,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'django>=1.7',
        'urllib3',
        'bunch'
    ],
)

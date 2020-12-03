# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from aldryn_haystack import __version__


REQUIREMENTS = [
    'aldryn-django',
    'elasticsearch',
    'requests-aws4auth',
    'django-haystack',
    'furl',
    'django-getenv',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 3.0',
    'Framework :: Django :: 3.1',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='aldryn-haystack',
    version=__version__,
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/aldryn-haystack',
    license='BSD',
    description='An opinionated haystack setup bundled as an Aldryn Addon.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)

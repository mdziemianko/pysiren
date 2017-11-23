from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup, find_packages

__author__ = 'Tim Martin'
__pkg_name__ = 'ripozo'

version = '0.1.0'

setup(
    author=__author__,
    author_email='tim.martin@vertical-knowledge.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description='Utility for generating Siren Hypermedia compliant payloads.',
    extras_require={
        'docs': [
            'sphinx'
        ]
    },
    install_requires=[
    ],
    keywords='REST HATEOAS Hypermedia RESTful SIREN HAL API JSONAPI web framework Django Flask SQLAlchemy Cassandra',
    name='ripozo',
    packages=find_packages(include=['ripozo', 'ripozo.*']),
    tests_require=[
        'nose',
    ],
    test_suite="tests",
    url='http://ripozo.readthedocs.org/',
    version=version
)
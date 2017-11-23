from setuptools import setup, find_packages

__author__ = 'Michal Dziemianko'
__pkg_name__ = 'pysiren'

version = '0.1.0'

setup(
    author=__author__,
    author_email='michal.dziemianko@gmail.com',
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
    name='pysiren',
    packages=find_packages(include=['pysiren', 'pysiren.*']),
    tests_require=[
        'nose',
    ],
    test_suite="test",
    url='https://github.com/mdziemianko/pysiren',
    version=version
)
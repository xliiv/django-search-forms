# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(name='django-search-forms',
    version='0.1',
    description="Search forms for django",
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
    keywords='django search forms',
    author='Szymon Pyżalski',
    author_email='szymon@pythonista.net',
    license='BSD',
    packages=find_packages(),
    zip_safe=True,
    install_requires=[
        'django',
    ]
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'numpy>=1.11',
    'fitsio>=0.9.10'
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(Hazboun6): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pdat',
    version='0.1.4',
    description="Python package for dealing with PSRFITS and other pulsar data files.",
    long_description=readme + '\n\n' + history,
    author="Jeffrey S Hazboun",
    author_email='jeffrey.hazboun@gmail.com',
    url='https://github.com/hazboun6/PulsarDataToolbox',
    packages=find_packages(include=['pdat']),
    entry_points={
        'console_scripts': [
            'pdat=pdat.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    keywords='pdat',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

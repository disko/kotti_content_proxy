# -*- coding: utf-8 -*-

"""
Created on 2014-09-23
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup

version = '0.3.0'
project = 'kotti_content_proxy'

install_requires = [
    'Kotti>=1.0.0',
]

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(
    name=project,
    version=version,
    description="A content type that proxies other content in a Kotti site",  # noqa
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Pyramid",
        "Intended Audience :: Developers",
        "License :: Repoze Public License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python",
    ],
    keywords='kotti addon',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/Kotti',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    entry_points={},
    extras_require={},
    message_extractors={
        'kotti_content_proxy': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)

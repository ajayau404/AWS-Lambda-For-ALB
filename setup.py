#!/usr/bin/env python
from setuptools import setup, find_packages


with open('README.md') as readme_file:
    README = readme_file.read()


install_requires = [
    'wheel',
    'setuptools'
]

setup(
    name='py-lambda',
    version='1.1.0',
    description="Lambda framework",
    long_description=README,
    author="Ajay A U",
    author_email='ajayau404@gmail.com',
    url='https://github.com/ajayau404/AWS-Py-Lambda',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
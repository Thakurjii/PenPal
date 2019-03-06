# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PenPal',
    version='0.1.0',
    description='Send Gmail using Command Line.',
    long_description=readme,
    author='Gaurav Thakur',
    author_email='gauravthakur40127@gmail.com',
    url='https://github.com/Thakurjii/PenPal',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


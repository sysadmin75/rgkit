#!/usr/bin/env python
'''
Run: ./setup.py register sdist upload
Check: ./setup.py checkdocs (pip install collective.checkdocs)
'''

from setuptools import setup

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='rgkit',
    version='1.0.0',
    description='Game Engine for Robot Game',
    maintainer='Kristopher Newsome',
    maintainer_email='kris@krisnewsome.com',
    url='https://github.com/sysadmin75/rgkit',
    packages=['rgkit', 'rgkit.render'],
    package_data={'rgkit': ['bots/*.py', 'maps/*.py']},
    license='Unlicense',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'rgrun = rgkit.run:main',
            'rgmap = rgkit.mapeditor:main'
        ]
    },
)

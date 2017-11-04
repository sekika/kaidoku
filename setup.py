# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import configparser

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Read version from kaidoku/data/system.ini

inifile = configparser.ConfigParser()
inifile.read(path.join(here, 'kaidoku/data/system.ini'))
version = inifile.get('system', 'version')

setup(
    name='kaidoku',
    version=version,
    description='Player, solver and creater of sudoku puzzles',
    long_description=long_description,
    url='https://sekika.github.io/kaidoku/',
    author='Katsutoshi Seki',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment :: Puzzle Games'
    ],
    packages=['kaidoku'],
    package_data={'kaidoku': ['data/sudoku.*', 'data/system.ini']},
    install_requires=['ConfigObj', 'pillow', 'pyx'],
    entry_points={  
        'console_scripts':  
            'kaidoku = kaidoku.main:main'  
    },
)

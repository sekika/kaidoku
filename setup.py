# -*- coding: utf-8 -*-

from setuptools import setup
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
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: JavaScript',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Natural Language :: Japanese',
        'Topic :: Games/Entertainment :: Puzzle Games'
    ],
    keywords='sudoku',
    packages=['kaidoku'],
    package_data={'kaidoku': ['data/*']},
    install_requires=['ConfigObj', 'pillow', 'pyx', 'tk'],
    python_requires=">=3.5",
    entry_points={
        'console_scripts':
            'kaidoku = kaidoku.main:main'
    },
)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kaidoku',
    version='0.0.1',
    description='Player, solver and creater of sudoku puzzles',
    long_description=long_description,
    url='https://github.com/sekika/kaidoku',
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
#    install_requires=['numpy', 'scipy'],
    entry_points={  
        'console_scripts':  
            'kaidoku = kaidoku.main:main'  
    },
)

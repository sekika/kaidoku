#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo 'flake8'
flake8 ../kaidoku/*.py | sed -e 's/^.*kaidoku\///' > flake8.txt
grep -v E501 flake8.txt
kaidoku test

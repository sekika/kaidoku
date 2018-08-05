#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo 'flake8'
flake8 ../kaidoku/*.py | sed -e 's/^.*kaidoku\///' | grep -v E501
kaidoku test
# Check description
echo "Checking README.rst."
python3 ../setup.py --long-description | rst2html.py > /dev/null

#!/bin/sh
echo 'flake8'
flake8 ../kaidoku/*.py | sed -e 's/^.*kaidoku\///' > flake8.txt
grep -v E501 flake8.txt
echo 'kaidoku test'
kaidoku test > test.txt
diff test-pre.txt test.txt > diff.txt
cp test.txt test-pre.txt
wc -l *.txt | grep -v total

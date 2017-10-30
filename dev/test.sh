#!/bin/sh
echo 'flake8'
flake8 ../kaidoku/*.py | grep -v E501
echo 'kaidoku test'
kaidoku test > test.txt
diff test-pre.txt test.txt > diff.txt
cp test.txt test-pre.txt
wc -l *.txt | grep -v total
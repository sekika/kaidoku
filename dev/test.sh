#!/bin/sh
echo 'Testing'
kaidoku test > test.txt
diff test-pre.txt test.txt > diff.txt
cp test.txt test-pre.txt
wc -l *.txt | grep -v total

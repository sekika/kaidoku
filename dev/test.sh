#!/bin/sh
echo 'Testing'
kaidoku test > test.txt
diff test-pre.txt test.txt
cp test.txt test-pre.txt

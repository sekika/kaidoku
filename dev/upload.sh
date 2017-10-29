#!/bin/sh
LATEST=`pip3 search kaidoku | grep ^kaidoku | awk '{print $2}' | sed -e 's/(//' | sed -e 's/)//'`
echo 'Latest version: '$LATEST
CURRENT=`grep ^version ../kaidoku/data/system.ini | sed -e 's/^.*=//' | sed -e 's/ //g'`
echo 'Development version: '$CURRENT
if [ $LATEST = $CURRENT ]; then
  echo 'Change version in ../kaidoku/data/system.ini to upload.'
  exit
fi
echo "Making packages."
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel
echo "Preparing PyPI password with passme"
# pip3 install passme
passme python
twine upload "dist/kaidoku-"$CURRENT*
pip3 uninstall kaidoku
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "pip3 install kaidoku"

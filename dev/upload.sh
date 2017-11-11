#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`

# Install the source
echo "Installing the source"
pip3 install -e .. > /dev/null

# Test
sh test.sh

exit #####

# Check version
LATEST=`pip3 search kaidoku | grep ^kaidoku | awk '{print $2}' | sed -e 's/(//' | sed -e 's/)//'`
echo 'Latest version: '$LATEST
CURRENT=`grep ^version ../kaidoku/data/system.ini | sed -e 's/^.*=//' | sed -e 's/ //g'`
echo 'Development version: '$CURRENT
if [ $LATEST = $CURRENT ]; then
  echo 'Change version in ../kaidoku/data/system.ini to upload.'
  exit
fi

# Document version
echo "Rewriting document"
cd ../docs
cat _config.yml | sed -e "s/^version:.*$/version: $CURRENT/" > tmp
mv tmp _config.yml
git add _config.yml
git commit -m "version "$CURRENT
git push

# Make package
echo "Making packages."
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel

# Upload
echo "Preparing PyPI password with passme"
# pip3 install passme
passme python
twine upload "dist/kaidoku-"$CURRENT*

# Uninstall kaidoku
pip3 uninstall kaidoku
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "pip3 install kaidoku"


all:

deb:
	python3 setup.py --command-packages=stdeb.command bdist_deb

# -*- coding: utf-8 -*-
"""Main modules.

Start from main()
"""
import configparser
import os.path
import sys

from configobj import ConfigObj

from kaidoku.command import command
from kaidoku.help import welcommessage
from kaidoku.misc import openappend

# Kaidoku starts here


def main(argv=sys.argv[1:]):
    """Main module."""
    # Read system configuration from data/system.ini
    inifile = configparser.ConfigParser()
    here = os.path.abspath(os.path.dirname(__file__))
    inifile.read(os.path.join(here, 'data/system.ini'))
    version = inifile.get('system', 'version')
    ConfFile = os.path.expanduser(inifile.get('file', 'config'))

    # Read user configuration
    config = readconfig(ConfFile)
    # configuration file can be redirected
    while 'redirect' in config:
        ConfFile = os.path.expanduser(config['redirect'])
        config = readconfig(ConfFile)

    # Kaidoku command line
    if (len(sys.argv)) == 1:
        print(welcommessage(version))
        while True:
            try:
                arg = input('kaidoku-' + version + '> ').strip().split()
            except Exception:
                print('\nQuitting kaidoku.')
                return
            if len(arg) > 0:
                if arg[0] == 'q':
                    print('Quitting kaidoku.')
                    return
                config = command(arg, config)
                config.write()
    else:
        arg = sys.argv[1:]
        config = command(arg, config)
        config.write()
        return


def readconfig(ConfFile):
    """Read configuration."""
    from PIL import ImageFont

    # Read configuration
    config = ConfigObj(os.path.expanduser(ConfFile), encoding='utf-8')

    # Return if it has redirect
    if 'redirect' in config:
        return config

    # Read system default configuration from data/system.ini
    inifile = configparser.ConfigParser()
    here = os.path.abspath(os.path.dirname(__file__))
    inifile.read(os.path.join(here, 'data/system.ini'))
    defaultLevel = inifile.get('default', 'level')
    defaultMaxtime = inifile.get('default', 'maxtime')
    defaultSymmetry = inifile.get('default', 'symmetry')
    defaultMincell = inifile.get('default', 'mincell')
    defaultAxis = inifile.get('default', 'axis')
    fonts = inifile.get('default', 'font').split()

    # Set default configuration
    if 'datadir' in config:
        datadir = os.path.expanduser(config['datadir'])
        if not os.path.isdir(datadir) and datadir != '':
            try:
                os.mkdir(datadir)
            except Exception:
                print('Error: directory cannot be created.', datadir)
                datadir = ''
    else:
        datadir = ''
    config['datadir'] = datadir
    if 'file' in config:
        file = os.path.expanduser(config["file"])
        if os.path.exists(file):
            try:
                input = open(file, 'r')
                input.close()
            except Exception:
                out = openappend(file)
                if out == '':
                    print('Cannot open file:', file)
                    sys.exit()
                out.close()
            config["file"] = file
        else:
            print(file + ' does not exist.')
            file = os.path.abspath(os.path.dirname(__file__)) + '/data/sudoku.txt'
            print('Changing to default file: ' + file)
            config['file'] = file
    else:
        file = os.path.abspath(os.path.dirname(__file__)) + '/data/sudoku.txt'
        config["file"] = file
    if 'file2' in config:
        file2 = os.path.expanduser(config["file2"])
    else:
        if file != '':
            name, ext = os.path.splitext(file)
            file2 = name + '2' + ext
            config["file2"] = file2
        else:
            file2 = ''
    if 'giveup' in config:
        giveup = os.path.expanduser(config["giveup"])
    else:
        giveup = ''
        config["giveup"] = giveup
    if 'level' in config:
        level = config["level"]
    else:
        level = defaultLevel
        config["level"] = level
    if 'maxtime' in config:
        maxtime = config["maxtime"]
    else:
        maxtime = defaultMaxtime
        config["maxtime"] = maxtime
    if 'pointer' in config:
        pointer = config["pointer"]
    else:
        pointer = [''] + [1] * 9
        config["pointer"] = pointer
    if 'move' not in config:
        config["move"] = []
    if 'bookmark' in config:
        bookmark = config["bookmark"]
    else:
        bookmark = {}
        config["bookmark"] = bookmark
    if 'create' not in config:
        config['create'] = {}
    if 'symmetry' not in config['create']:
        config['create']['symmetry'] = defaultSymmetry
    if 'minlevel' not in config['create']:
        config['create']['minlevel'] = 1
    if int(config['create']['minlevel']) < 1:
        config['create']['minlevel'] = 1
    if int(config['create']['minlevel']) > 9:
        config['create']['minlevel'] = 1
    if 'mincell' not in config['create']:
        config['create']['mincell'] = defaultMincell
    if 'figure' not in config:
        config['figure'] = {}
    if 'font' not in config['figure']:
        for font in fonts:
            try:
                ImageFont.truetype(font, int(16))
                config['figure']['font'] = font + '.ttf'
                break
            except Exception:
                continue
            config['figure']['font'] = 'NotFound'
    if 'color' not in config['figure']:
        config['figure']['color'] = 'black'
    if 'lastcolor' not in config['figure']:
        config['figure']['lastcolor'] = 'green'
    if 'normalsize' not in config['figure']:
        config['figure']['normalsize'] = 'medium'
    if 'markedsize' not in config['figure']:
        config['figure']['markedsize'] = 'large'
    if 'axis' not in config['figure']:
        config['figure']['axis'] = defaultAxis
    config.write()
    return config

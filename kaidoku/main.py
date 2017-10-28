# -*- coding: utf-8 -*-
import sys, os.path, warnings
from configobj import ConfigObj
from .command import (command)
from .misc import (openappend)
from .help import (welcommessage)

# Kaidoku starts here

def main(argv=sys.argv[1:]):    

    # Hard-coded configuration
    version = '0.0.1'
    ConfFile = os.path.expanduser('~/.kaidoku') # Filename of the config file

    # Read configuration from the config file
    config = readconfig(ConfFile)
    
    # Kaidoku command line
    if (len(sys.argv)) == 1:
        print (welcommessage(version))
        while True:
            try:
                arg = input('kaidoku-'+version+'> ').strip().split()
            except:
                print ('\nQuitting kaidoku.')
                return
            if arg[0] == 'q':
                print ('Quitting kaidoku.')
                return
            config = command(arg, config)
            config.write()
    else:
        arg = sys.argv[1:]
        config = command(arg, config)
        config.write()
        return

# Read configuration

def readconfig(ConfFile):
    config = ConfigObj(os.path.expanduser(ConfFile), encoding='utf-8')
    
    if 'file' in config:
        file =  os.path.expanduser(config["file"])
        try:
            input = open(file, 'r')
            input.close()
        except:
            out = openappend (file)
            if out == '':
                print ('Cannot open file:', file)
                sys.exit()
            out.close
        config["file"] = file
    else:
        file = os.path.abspath(os.path.dirname(__file__))+'/data/sudoku.txt'
        config["file"] = file
    if 'file2' in config:
        file2 =  os.path.expanduser(config["file2"])
    else:
        if file != '':
            name, ext = os.path.splitext(file)
            file2 = name + '2' + ext
            config["file2"] = file2
        else:
            file2 = ''
    if 'giveup' in config:
        giveup =  os.path.expanduser(config["giveup"])
    else:
        giveup = ''
        config["giveup"] = giveup
    if 'level' in config:
        level = config["level"]
    else:
        level = 2
        config["level"] = level
    if 'maxtime' in config:
        maxtime = config["maxtime"]
    else:
        maxtime = 60
        config["maxtime"] = maxtime
    if 'pointer' in config:
        pointer = config["pointer"]
    else:
        pointer = [''] + [1] * 9
        config["pointer"] = pointer
    if 'move' in config:
        move = config["move"]
    else:
        config["move"] = []
    if 'bookmark' in config:
        bookmark = config["bookmark"]
    else:
        bookmark = {}
        config["bookmark"] = bookmark
    config.write()
    return config

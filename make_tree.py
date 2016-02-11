import os
from subprocess import call
import sys
import json
def help():
    with open("readme.txt", 'r') as readme:
        for line in readme.readlines():  print(line)
def run_editor():     #if there is "-r"-flag => run FILES
    make_tree()
<<<<<<< HEAD
    for arg in ARGS: 
        for var in VAR_PATH:
            if arg in os.listdir(var): EDITOR = [arg,]
=======
    for arg in ARGS:
        if arg in os.listdir('/usr/bin'): EDITOR = [arg,]
>>>>>>> a5fcf35e27043345f98648208320eee82e1a0771
    call(EDITOR+FILES)     #flag set new EDITOR "arg"
def repeater(path, root):
    i = 1
    main = root
    while root in os.listdir(path):     #check is there directory with the same name as our root
        root = main + str(i)
        i+=1
    return root
def make_tree():
    root_dir = "web_project_x"     #root directory for project
    path = os.getcwd()    # default path to make tree is current directory
    for arg in ARGS:
        if ('/' in arg): path = arg     #flag set new path to project directory
    path += '/' + repeater(path, root_dir) + '/'
    for directory in DIRS: os.mkdir(path+directory)    #make tree of directories
    for file_name in FILES:
        with open(path+file_name, "w") as f:     #create main FILES
            if (".html" in file_name): f.write('!')     #for Emmet
            elif (".js" in file_name): f.write('$(document).ready(main);\n\
                var main = function(){\n/*<--script-->*/\n})')     #template
def read_flags():
    flags = {'-h': help, '--help': help, '-r': run_editor}
    for arg in ARGS:
        if arg in flags.keys():
            flags[arg]()
            return 0
    make_tree()
ARGS = sys.argv[1:]     #remove name of script from arguments
with open("source.json", 'r') as out: data = out.read()
<<<<<<< HEAD
EDITOR, DIRS, FILES = json.loads(data)['EDITOR'], json.loads(data)['DIRS'], json.loads(data)['FILES']
VAR_PATH = os.environ['PATH'].split(':')
=======
       #default EDITOR to open FILES after creation tree
EDITOR, DIRS, FILES = json.loads(data)['EDITOR'], json.loads(data)['DIRS'], json.loads(data)['FILES']
>>>>>>> a5fcf35e27043345f98648208320eee82e1a0771
read_flags()
import os
import sys
import json
from editor import run_editor as run_editor
def help():
    with open("readme.txt", 'r') as readme:
        for line in readme.readlines():  print(line)
def run():
    run_editor(ARGS, make_tree())
def checker(path, root):
    i = 1
    main = root
    while root in os.listdir(path):     #check is there directory with the same name as our root
        root = main + str(i)
        i+=1
    return root
def make_tree():
    path = os.getcwd()    # default path to make tree is current directory
    for arg in ARGS:
        if os.path.isdir(arg): path = arg     #flag set new path to project directory
    path += '/' + checker(path, root_dir) + '/'
    for directory in DIRS: os.mkdir(path+directory)    #make tree of directories
    for file_name in FILES:
        with open(path+file_name, "w") as f:
            f.write(FILES[file_name])
    return path
def read_flags():
    for arg in ARGS:
        if arg in FLAGS.keys():
            globals()[FLAGS[arg]]()
            return 0
    return 1
ARGS = sys.argv[1:]     #remove name of script from arguments
path =''
with open("source.json", 'r') as out: data = out.read()
root_dir, DIRS, FILES, FLAGS = json.loads(data)['ROOT_DIR'], json.loads(data)['DIRS'], json.loads(data)['FILES'], json.loads(data)['FLAGS']
if read_flags(): make_tree()

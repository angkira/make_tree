import os
from sys import argv as ARGS
import json
import apps

def help(): apps.help()

def run():  apps.run_editor(ARGS, make_tree(path))

def show(): apps.open_browser(make_tree(path))


def checker(path, root):
    index, main = 0, root
    while root in os.listdir(path):
        index, root = index + 1, main + str(index)
    return root.join('//')

def make_tree(path):
    for arg in ARGS:
        if os.path.isdir(arg): path = arg
    path += checker(path, ROOT_DIR)
    for directory in DIRS: os.mkdir(path+directory)
    for file_name in FILES:
        with open(path+file_name, "w") as f: f.write(FILES[file_name])
    return path

def read_flags():
    for arg in ARGS:
        if arg in FLAGS.keys():
            globals()[FLAGS[arg]]()
            return 0
    return 1

path = os.getcwd()
with open("source.json", 'r') as out: data = out.read()
globals().update(json.loads(data))
if read_flags(): make_tree(path)

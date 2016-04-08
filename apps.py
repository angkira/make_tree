import os
import json

with open("source.json", 'r') as file:
    data = file.read()
globals().update(json.loads(data))
operations = ['run_editor', 'open_browser']


def checkFlags(flags):
    if flags == '-help':
        help()
    else:
        for flag in flags:
            if flag not in FLAGS.keys():
                print("Sorry, wrong flags!")
                help()
                return 0
        return 1


def readFlags(flags, ARGS):
    if checkFlags(flags):
        make_tree(ARGS)
        for flag in flags:
            globals()[FLAGS[flag]]()


def setTemplate():
    for arg in ARGS:
        if arg[0] == '+':
            globals().update({'TEMPLATE': arg[1:]})
    with open('templates.json', 'r') as temp_file:
        temp_info = temp_file.read()
        globals().update(json.loads(temp_info)[TEMPLATE])


def init(ARGS):
    globals().update({'ARGS': ARGS})


def help():
    with open("help.txt", 'r') as help_text:
        print(help_text.read())


def make_tree(ARGS):
    init(ARGS)
    setTemplate()
    for arg in ARGS:
        if os.path.isdir(arg):
            os.chdir(arg)
    root, index = ROOT_DIR, 0
    while root in os.listdir(os.getcwd()):
        index, root = index + 1, ROOT_DIR + str(index)
    globals().update({'ROOT_DIR': root})
    os.mkdir(ROOT_DIR)
    os.chdir(ROOT_DIR)
    for directory in DIRS:
        os.mkdir(directory)
    for file_name in FILES:
        with open(file_name, "w") as f:
            f.write(FILES[file_name])


def run_editor():
    for arg in ARGS[1:]:
        for folder in os.environ['PATH'].split(os.pathsep):
            if os.path.isdir(folder) and arg in os.listdir(folder):
                EDITOR = [folder+'/'+arg, ]
    os.system(globals()['EDITOR']+' '+os.getcwd()+'/'+ROOT_DIR+'/'+' -n')


def open_browser():
    if os.name == 'nt':
        BROWSER = 'start '
    os.system(globals()['BROWSER']+' '+os.getcwd()+'/'+'index.html')

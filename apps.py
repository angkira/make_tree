import os
import json

with open("source.json", 'r') as file: data = file.read()
globals().update(json.loads(data))

def init(ARGS):
    globals().update({'ARGS':ARGS})

def help():
    with open("help.txt", 'r') as help_text: print(help_text.read())

def make_tree():    
    for arg in ARGS:
        if os.path.isdir(arg): os.chdir(arg)   
    root = ROOT_DIR
    main, index = root, 0
    while root in os.listdir(os.getcwd()):
        index, root = index + 1, main + str(index)
    globals().update({'root':root})
    os.mkdir(root)
    os.chdir(root) 
    for directory in DIRS: os.mkdir(directory)
    for file_name in FILES:
        with open(file_name, "w") as f: f.write(FILES[file_name])

def run_editor():
    for arg in ARGS[1:]:
        for folder in os.environ['PATH'].split(os.pathsep):
            if os.path.isdir(folder) and arg in os.listdir(folder): 
                EDITOR = [folder+'/'+arg,]
    edit = os.popen(globals()['EDITOR']+' '+os.getcwd()+'/'+root+'/'+' -n')

def open_browser():
    if os.name == 'nt': BROWSER = 'start '
    call(globals()['BROWSER']+' '+os.getcwd()+'/'+'index.html', shell = True)
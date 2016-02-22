import os
from subprocess import call
import json
with open("source.json", 'r') as out: data = out.read()


def help():
    with open("help.txt", 'r') as help_text: print(help_text.read())

def run_editor(ARGS, path):
	EDITOR, files = json.loads(data)['EDITOR'], json.loads(data)['FILES'].keys()
	for arg in ARGS[1:]:
		for folder in os.environ['PATH'].split(os.pathsep):
			if os.path.isdir(folder) and arg in os.listdir(folder): EDITOR = [folder+'/'+arg,]
	call(EDITOR+[path+file_ for file_ in files], shell=True)

def open_browser(path):
	BROWSER = 'start ' if os.name == 'nt' else json.loads(data)['BROWSER']
	call(BROWSER+' '+path+'index.html', shell = True)
run_editor('brackets', os.getcwd())

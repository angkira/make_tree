import sys
from subprocess import call
import json
with open("source.json", 'r') as out: data = out.read()


def help():
    with open("help.txt", 'r') as help_text: print(help_text.read())

def run_editor(ARGS, path):
	EDITOR, files = json.loads(data)['EDITOR'], json.loads(data)['FILES'].keys()
	for arg in ARGS[1:]:
		for folder in sys.path:
			if arg in folder: EDITOR = [arg,]
	call(EDITOR+[path+file_ for file_ in files], shell=True)

def open_browser(path):
	BROWSER = 'start ' if sys.platform == 'win32' else json.loads(data)['BROWSER']
	call(BROWSER+' '+path+'index.html', shell = True)

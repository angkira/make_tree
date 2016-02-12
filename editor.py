import sys
from subprocess import call
import json
with open("source.json", 'r') as out: data = out.read()
def run_editor(ARGS, path):     #if there is "-r"-flag => run FILES
	EDITOR, files = json.loads(data)['EDITOR'], json.loads(data)['FILES'].keys()
	for arg in ARGS:
	    for var in VAR_PATH:
	        if arg in sys.path: EDITOR = [arg,]#flag set new EDITOR "arg"
	print (path)
	call(EDITOR+[path+file for file in files])

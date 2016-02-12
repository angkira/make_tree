import os
from subprocess import call
import json
with open("source.json", 'r') as out: data = out.read()
def run_editor(ARGS, path):     #if there is "-r"-flag => run FILES
	VAR_PATH = os.environ['PATH'].split(':')
	EDITOR, files = json.loads(data)['EDITOR'], json.loads(data)['FILES'].keys()
	for arg in ARGS: 
	    for var in VAR_PATH:
	        if arg in os.listdir(var): EDITOR = [arg,]#flag set new EDITOR "arg"
	print path
	call(EDITOR+[path+file for file in files])     
import json
import os

data = dict(
	ROOT_DIR = "web_project_x",
	DIRS = ["css", "script", "img"],
	FILES = {'index.html': '!',\
			 'css/style.css':'',\
			 'script/common.js':'$(document).ready(main);\nvar main = function(){\n/*<--script-->*/\n}'},
	FLAGS = {'-h': 'help', '--help': 'help',
			 '-r': 'run_editor', '-R':'run_editor', '--run':'run_editor',
			 '-s': 'open_browser', '-S': 'open_browser', '--show': 'open_browser'},
	BROWSER = 'google-chrome-beta',
	EDITOR = 'subl3')

if not data['EDITOR']:
	data.update(EDITOR = 'notepad' if os.name == 'nt' else 'atom')
data = json.dumps(data, indent=4)
with open('source.json', 'w') as out:
	out.write(data)

import json
import os
data = dict(
ROOT_DIR	 = "web_project_x",
EDITOR 		 = ["atom",],
DIRS  		 = ["","css","script","img"],
FILES  		 = {'index.html': '!','css/style.css':'','script/common.js':'$(document).ready(main);\nvar main = function(){\n/*<--script-->*/\n}'},
FLAGS  		 = {'-h': 'help', '--help': 'help', '-r': 'run'})
data = json.dumps(data, indent=2)
with open('source.json', 'w') as out:
	out.write(data)


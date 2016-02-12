import json
#EDITOR = ["subl",]
#DIRS = ("","css","script","img")
#FILES = ["index.html","css/style.css","script/common.js"]
#FLAGS = {'-h': help, '--help': help, '-r': run_editor}
data = json.dumps(dict(FLAGS = {'-h': 'help', '--help': 'help', '-r': 'run_editor'}, EDITOR = ["subl",], DIRS = ("","css","script","img"), FILES = ["index.html","css/style.css","script/common.js"]), indent=2)
with open("source.json",'w') as out:
    out.write(data)
#with open("source.json",'r') as out:
    #out.read(data)
#dirs,files = json.loads(data)['DIRS'],json.loads(data)['FILES']
#print dirs,files

import json
EDITOR = ["subl",]
DIRS = ("","css","script","img")
FILES = ["index.html","css/style.css","script/common.js"]
data = json.dumps(dict(EDITOR = ["subl",], DIRS = ("","css","script","img"), FILES = ["index.html","css/style.css","script/common.js"]), indent=2)
with open("source.json",'a') as out:
    out.write(data)
#with open("source.json",'r') as out:
    #out.read(data)
#dirs,files = json.loads(data)['DIRS'],json.loads(data)['FILES']
#print dirs,files
#94:51:a8:de:5d:2b:08:32:59:64:e9:31:fa:f2:41:1f

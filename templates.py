import json

data = dict(
    simple=dict(
        DIRS=["css", "script", "img"],
        FILES={'index.html': '!',
               'css/style.css': '',
               'script/common.js': '$(document).ready(main);\nvar main = function(){\n/*<--script-->*/\n}'
               }),
    jade=dict(
        DIRS=["css", "script", "img"],
        FILES={'index.jade': 'extends layout',
               'layout.jade': "doctype html\
                                    \n\thtml\
                                    \n\t\thead\
                                    \n\t\t\ttitle= title\
                                    \n\t\t\tlink(rel='stylesheet', href='/stylesheets/style.css')\
                                    \n\t\tbody\
                                    \n\t\t\tblock content',",
               'css/style.css': "",
               'script/common.js': '$(document).ready(main);\nvar main = function(){\n/*<--script-->*/\n}'
               }
    ),
    jade_sass=dict(
        DIRS=["css", "script", "img"],
        FILES={'index.jade': 'extends layout',
               'layout.jade': "doctype html\n\thtml\n\t\thead\n\t\t\ttitle= title\\n\t\t\tlink(rel='stylesheet', href='/stylesheets/style.css')\n\t\tbody\n\t\t\tblock content',",
               'css/style.sass': "",
               'script/common.js': '$(document).ready(main);\nvar main = function(){\n/*<--script-->*/\n}'
               }
    ))

data = json.dumps(data, indent=4)
with open('templates.json', 'w') as out:
    out.write(data)

import json
import os

data = dict(
    ROOT_DIR="web_project_x",
    TEMPLATE="simple",
    FLAGS={'h': 'help', '-help': 'help',
           'r': 'run_editor', 'R': 'run_editor',
           's': 'open_browser', 'S': 'open_browser',
           't': 'setTemplate',},
    BROWSER='firefox',
    EDITOR='atom')

if not data['EDITOR']:
    data.update(EDITOR='notepad' if os.name == 'nt' else 'atom')
data = json.dumps(data, indent=4)
with open('source.json', 'w') as out:
    out.write(data)

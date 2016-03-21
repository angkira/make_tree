from sys import argv as ARGS
from apps import *

def read_flags():
    FLAGS = json.loads(data)['FLAGS']
    for arg in ARGS:
        if !(arg in FLAGS.keys()) and (FLAGS[arg] == 'help'):
            help()
            break
        else:
            init(ARGS)
            make_tree()
            if arg in FLAGS.keys():
                globals()[FLAGS[arg]]()

read_flags()

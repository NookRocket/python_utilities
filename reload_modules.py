import sys
import importlib
modules = sys.modules.copy()
removed_mod = {}
# Specify the prefix to avoid reload negligible modules
prefix_module = '' # e.g 'snow.'

for key, module in modules.items():
    if key.startswith(prefix_module) and module:
        if module:
            removed_mod[key] = module
            del sys.modules[key]

for key, module in removed_mod.items(): 
    try:
        importlib.import_module(key, module)
    except Exception as err:
        print('Error reload module : {} : {}'.format(key, err))

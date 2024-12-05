import sys
import importlib
modules = sys.modules.copy()
removed = {}
for key, module in modules.items():
    if key.startswith('snow.') and module:
        if module:
            removed[key] = module
            del sys.modules[key]

for key, module in removed.items(): 
    try:
        importlib.import_module(key, module)
    except Exception as err:
        print('Error reload module : {} : {}'.format(key, err))

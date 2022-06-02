import os
import traceback
from importlib import util
'''
This file contains:
1. The Base Plugin, that holds all plugins that are available in this directory
2. A function that loads a module from a file-path
3. Code that is run in order to setup the Base-Class Plugin List
'''

#1.
class Base:
    """Basic resource class. Concrete resources will inherit from this one
    """
    plugins  = {}
    main_cls = None

    def __init__(self,main):
        self.main_cls=main
    # For every class that inherits from the current,
    # the class name will be added to plugins
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        name=cls.__name__
        cls.plugins[name]=cls

    def set_main_value(self):
        '''
        Example: Base function that is avialable for all plugins. (Might be overwritten by child)
        :return:
        '''
        print("Set main value to 3")
        self.main_cls.main_value=3


#2.
# Small utility to automatically load modules
def load_module(path):
    name = os.path.split(path)[-1]
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

#3.
# Get current path
path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    # Load only "real modules"
    if not fname.startswith('.') and \
       not fname.startswith('_') and fname.endswith('.py'):
        try:
            load_module(os.path.join(dirpath, fname))
        except Exception:
            traceback.print_exc()
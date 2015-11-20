import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
from base import * # required because that is what we will override

# now first import dev
if os.path.isfile(os.path.join(ROOT_DIR, 'settings/dev.py')):  
    from dev import *
# and then import prod because that has to override all the settings
if os.path.isfile(os.path.join(ROOT_DIR, 'settings/prod.py')):  
    from prod import * 

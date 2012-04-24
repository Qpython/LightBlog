import os,sys,bottle

sys.path = ['/var/www/blog/'] + sys.path
os.chdir(os.path.dirname(__file__))

import main
 
application = bottle.default_app()

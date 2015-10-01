import sys, os
# get path of the tornado project
path = ("/").join( sys.path[0].split("/")[:-1])
print path
if path not in sys.path:
    sys.path.append(path)

#demarage de django
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoproject.settings'

from django import setup
setup()

from zephserver.main import main
main()

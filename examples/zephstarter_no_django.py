import sys, os
# get path of the tornado project
path = ("/").join( sys.path[0].split("/")[:-1])
print path
if path not in sys.path:
    sys.path.append(path)


from zephserver.main import main
main()

==================
Command line tools
==================
The server comes with three commands when you install it. Two are standard and already implemented and the third is documented and not implemented yet.
All command must be called in the folder where you can find the zephsettings.py file

Zephserver-start
================
When you use zephserver as a standalone (not with Django or an other framework which needs to be started)  you can start zephserver by going to the folder where is the zephsettings.py file and simply call the *zephserver-start* command. It takes no arguments and it will start the server in the shell you are currently using (and block it). To leave the server **DO NOT PRESS CTRL+C** or other kill method. If you do so You will have some cleaning to do prior to restart the server. Instead in an other shell (or in the same if you called it using the *&* in unix shell) call the *zephserver-stop* command in the same folder.

Zephserver-stop
===============
To kill the server, go to the folder where zephserver has been started and call *zephserver-stop*

Behind the scene it calls *zephserver-command stop* command.

Zephserver-command
==================
This is the generic command. It transmits its arguments as string to the server. Currently the only valid argument is *stop*.

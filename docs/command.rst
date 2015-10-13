==================
Command line tools
==================
The server comes with three commands when you install it. Two are standard and already implemented and the third is documented and not implemented yet.
All command must be called in the folder where you can find the zephsettings.py file

Zephserver-stop
===============
To kill the server, go to the folder where zephserver has been started and call *zephserver-stop*

Currently you have to specify the path to the socket example : *zephserver-stop /var/sock/zephserver.sock*

Behind the scene it calls *zephserver-command stop* command.

Zephserver-command
==================
This is the generic command. It transmits its arguments as string to the server. Currently the only valid argument is *stop*.

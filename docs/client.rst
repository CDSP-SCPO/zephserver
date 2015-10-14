============================
Zephserver javascript client
============================

This document only speaks about the javascript API for zephserver. For more informations about Zephserver go to main documentation_

.. _documentation : index.html 

Zephserver uses a simple protocol based on JSON to communicate with the server.

This protocol is too unstable to be documented and it is strongly advised to use the provided javascript library as client.

Zephclient object
-----------------
The library is on simple javascipt object. The constructopr is :

``Zephclient(session, url, room, messageCallback)`` 

-session is a string containning the session token (only used if you are using the django session and not on the same domain) it is optional

-url if the full url with port to the zephserver server (ie: wss://domaine.tld:8080/foo). It is optional, if you leave it undefined it will be ws://domain.tld/ws where domaine.tld is the current used domain

-room is the room your user will use. This argument is optional if undefined it will be the full path of the current page(the content of the window.location.href variable)

-messageCallback this variable is a function and can override the default callback (and the subscriber system). It is strongly advised to leave undefined.

None of the arguments are mandatory.

Send
----

The send method is used to send a message to the server. its prototype is 

``send(task, data)``

where :

-task is a string containing the short name of the task (ie : taskEcho). This argument is mandatory

-data is a json serializable object containing data ton give to the task. This argument is mandatory or not... depending of your task.

Subscribe
---------
This method is only available if you have left messageCallback undefined. 

The method permit to subscribe to a task. It means, each time this task will speaks you will receive the event.

``subscribe(task, callback)``

-task is a string giving the short name of the task (ie : taskEcho)

-callback is a function to call when the task speaks.

Unsuscribre
-----------
This method is only available if you have left messageCallback undefined. 

This method remove the function from the registred callbacks for the given task

``unsubscribe(task, callback)``

-task is a string giving the short name of the task (ie : taskEcho)

-callback is a function to remove from the callbacks list.
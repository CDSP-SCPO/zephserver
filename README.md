# Zephserver
## Python service manager that can be used as a WebSocket server

Zephserver is a python service manager that can be used in a cluster.
It has been written to support a websocket server but it can be used for any other stuff needing full time services or cluster management.

## Quickstart

To use zephserver you will need python 2.7. It should not work on python 3 and a Unix compatible system.

### Quickstart as service manager

(use zephserver as a websocket server bellow)

#### 1.Install zephserver from pip 

`pip install zephserver`

#### 2.Create your folder

`mkdir myserver`

#### 3.Add the configuration file

take zephsettings.py file from the example folder.

the variable heart_beat_period, PORT_ZEPH and TASKS_PATH are not used

empty the service list(these services are made for the websocket server)

#### 4.Add the starter file

Copy zephstarter_no_django.py file in your folder


#### 5.Write your services

read the zephserver/service/service_interface.py file to know the minimum interface you have to implement.

#### 6.Register your service

Add your service to the SERVICE_LIST variable.

Respect the syntax `my_server.my_package.my_service/MyService` syntaxe.

example for the service_interface it would be `'zephserver.service.service_interface/ServiceInterface'`

nota : there is no need to the service object to have the same name as its file and there can be multiple services in a file.

#### 7.Start your server

To start your server in the current shell, simply call : `python zephstarter_no_django.py`.

tips: to not lock your shell user the ` &` modifier at the end of the command.

#### 8.Stop your server

to stop your server call `zephserver-stop /path/to/the/folder/interface.sock`

If the server died without the zephserver command (crash) you will have to remove the server.lock file.

### Quickstart as websocket server

#### 1.Install zephserver from pip 

`pip install zephserver`

#### 2.Create your folder

`mkdir myserver`

if you use django myserver will simply refer to the django site folder 

#### 3.Add the configuration file

take zephsettings.py file from the example folder.

#### 4.Add the starter file

If you use django Copy the zephstarter.py file otherwise copy zephstarter_no_django.py file in your folder

#### 7.Start your server

To start your server in the current shell, simply call : `python zephstarter.py`.

tips: to not lock your shell user the ` &` modifier at the end of the command.

#### 8.Stop your server

to stop your server call `zephserver-stop /path/to/the/folder/interface.sock`

If the server died without the zephserver command (crash) you will have to remove the server.lock file.
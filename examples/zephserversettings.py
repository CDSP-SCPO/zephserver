# -*- coding: utf-8 -*-
'''
Copyright 2015 
    Centre de données socio-politiques (CDSP)
    Fondation nationale des sciences politiques (FNSP)
    Centre national de la recherche scientifique (CNRS)
License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
'''

# from zephserver.main import main
# Ficher de configuration du serveur zeph

LOG_LEVEL = 'DEBUG'
LOG_PATH = './logs.log'

#fichier a utiliser sous unix pour communiquer entre l'utilitaire en ligne de commande et le serveur
CONFIGURATION_NETWORK_INTERFACE='./interface.sock'
CONFIGURATION_NETWORK_INTERFACE_SERVER = './interface.sock'

#liste des services a activer
SERVICE_LIST = [
	'zephserver.service.db_service/DbService',
    'zephserver.service.routeur_service/RouteurService',
    'zephserver.service.clientsocket_service/StartClientSocket',
]

TASKS_PATH = {
    'TaskInterface':'zephserver.task.task_interface/TaskInterface',
    'TaskPing':'zephserver.task.task_ping/TaskPing',
}

CLUSTER_SERVER_LIST = [
    {
    'hostname' : 'zephserver',
    'address' : 'localhost',
    'port' : 22631
    },
]

#fichier pour interdire le demarage de plusieurs serveur en meme temps
LOCK_FILE = './server.lock'

#temps entre deux apels force a la bdd ecprime en secondes
heart_beat_period = 1600

PORT_ZEPH = 8080

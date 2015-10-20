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

import os, sys
import json
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web 
import tornado.wsgi
from tornado import websocket
# django settings must be called before importing models

from zephserver.infra.cluster_adapter import ClusterAdapter
from zephserversettings import PORT_ZEPH, MY_ROOM_HANDLER, MY_SESSION_HANDLER

from zephserver.infra.service_manager import ServiceManager
from zephserver.service.service_interface import ServiceInterface

class SocketService(websocket.WebSocketHandler):
		
	def initialize(self):
		"""Store a reference to the "external" RoomHandler instance"""
		self._inmessage = {}
		self.__clientID = None
		self.__user = None
		self.__rh = ServiceManager.get_instance().get_service(MY_ROOM_HANDLER)
		self.__session = ServiceManager.get_instance().get_service(MY_SESSION_HANDLER)
	
	def check_origin(self, origin):
		return True
	
	def on_message(self, message):
		self.get_user(message)
		self._inmessage = json.loads(message)
		logging.info(message)
		self._inmessage["usersession"]= self.__user
		if "task" in self._inmessage:
			self._inmessage["cid"]= self.__cid
			service_manager = ServiceManager.get_instance()
			routeur_service = service_manager.get_service('zephserver.service.routeur_service/RouteurService')
			routeur_service.route(self._inmessage)
		else:
			logging.info(message)
			cid = self.__rh.add_roomuser(message, self.__user)	
			self.__cid = cid
			self.__rh.add_client_wsconn(self.__cid, self)


	def open(self):
		#logging.info("WebSocket opened for %s" % user)
		pass
	 
	def on_close(self):
		self.__rh.remove_client(self.__cid)

	def get_user(self, message):			
		self.__user = self.__session.get_current_user(self, message)
		
			
settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	
	} 
# map the Urls to the class		  

class StartSocket(ServiceInterface):
	
	_room_handler = None
	_cluster = None
	
	def main(self):
		
		logging.info('launching SocketService service')
		
		application = tornado.web.Application([
			(r"/ws", SocketService),
		], **settings)
		http_server = tornado.httpserver.HTTPServer(application)

		http_server.listen(PORT_ZEPH)
		tornado.ioloop.IOLoop.instance().start()
		logging.info('Tornado started')
	
	def disable(self):
		logging.warning('asking to stop SocketService service')
		tornado.ioloop.IOLoop.instance().stop()
		logging.info('Tornado stoped')

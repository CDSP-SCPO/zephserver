import logging
from zephserver.infra.service_manager import ServiceManager
from zephserver.service.service_interface import ServiceInterface

from zephserver.infra.cluster_adapter import ClusterAdapter
from zephserversettings import MY_ROOM_HANDLER
from threading import Thread, Event, Lock

class SaySocket(ServiceInterface):
	
	_room_handler = None
	_cluster = None
	_shutdown_event = Event()
	
	def main(self):
		self._room_handler = ServiceManager.get_instance().get_service(MY_ROOM_HANDLER)
		self._cluster = ClusterAdapter.get_instance()
		self._cluster.subscribe('say_socket_send', self.say_cluster_callback)
		logging.info('launching SaySocket service')
		self._shutdown_event.wait()
		self._shutdown_event.clear()
		
	
	def say(self, answer, from_cluster=False):
		if 'cid' not in answer and not from_cluster:
			self._cluster.send('say_socket_send', answer)
		if 'room' in answer:
			self._room_handler.send_to_room(answer["room"], answer)
		elif 'users' in answer:
			self._room_handler.send_to_users(answer["users"], answer)
		elif 'all' in answer:
			self._room_handler.send_to_all( answer)
		elif 'cid' in answer:
			self._room_handler.send_to_cid(answer["cid"], answer)
	
	def say_cluster_callback(self, cluster_data):
		self.say(cluster_data['data'], True)
	
	def disable(self):
		logging.warning('asking to stop SaySocket service')
		self._shutdown_event.set()
		
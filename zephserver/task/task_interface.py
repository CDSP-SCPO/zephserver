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


class TaskInterface(object):
	'''
		task's model
		the interupt method HAS TO turn off fast for the server 
		shut down when the method "interrupt" is called
		main replaces the "run" method
	'''
	_request = None
	def __init__(self, request):
		self._request = request


	def main(self):
		'''
			main thread's method
		'''
		pass


	def interrupt(self):
		'''
			method asking task's death
			has to run fast (the method !)
		'''
		pass

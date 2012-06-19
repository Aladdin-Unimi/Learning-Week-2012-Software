# Copyright (C) 2012 Massimo Santini <massimo.santini@unimi.it>
#
# This file is part of Learning-Week-2012-Software (lw12).
# 
# Learning-Week-2012-Software is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
# 
# Learning-Week-2012-Software is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the GNU General
# Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# Learning-Week-2012-Software If not, see <http://www.gnu.org/licenses/>.

import yaml

class Dao( object ):
	
	def __init__( self, dikt, default = None ):
		self.__dikt = dikt
		self.default = default
	
	def __getattr__( self, attr ):
		try:
			return self.__dikt[ attr ]
		except KeyError:
			if self.default is not None: return self.default
			else: raise

	def keys( self ):
		return self.__dikt.keys()

	@staticmethod
	def daoize( data, default = None ):
		if isinstance( data, dict ):
			return Dao( data, default )
		elif isinstance( data, list ):
			return [ Dao.daoize( _, default ) for _ in data ]

def read_configs( yaml_string, default = None ):
	return Dao.daoize( yaml.load( yaml_string ), default )


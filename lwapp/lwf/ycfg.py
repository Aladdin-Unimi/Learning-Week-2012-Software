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

from xml.dom.minidom import parseString, Node

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
		if isinstance( data, unicode ):
			return data
		elif isinstance( data, dict ):
			return Dao( dict( ( k, Dao.daoize( v, default ) ) for k, v in data.items() ), default )
		elif isinstance( data, list ):
			return [ Dao.daoize( _, default ) for _ in data ]

def todict( e ):
	def traverse( e ):
		if e.nodeType == Node.TEXT_NODE:
			d = e.data.strip()
			if d: return d
			else: return None
		if e.nodeType != Node.ELEMENT_NODE and e.nodeType != Node.DOCUMENT_NODE: return None
		res = []
		for c in e.childNodes:
			s = traverse( c )
			if s: res.append( s )
		if len( res ) == 1 and isinstance( res[ 0 ], unicode ):
			return ( e.nodeName, res[ 0 ] )
		else:
			dres = dict()
			for k, v in res:
				if k in dres:
					if isinstance( dres[ k ], list ): dres[ k ].append( v )
					else: dres[ k ] = [ dres[ k ], v ]
				else:
					dres[ k ] = v
			return ( e.nodeName, dres )
	e.normalize()
	return dict( ( traverse( e.firstChild ), ) )

def read_configs( xml_string, default = None ):
	return Dao.daoize( todict( parseString( xml_string ) ), default )


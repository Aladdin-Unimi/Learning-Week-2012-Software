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

from io import BytesIO
from logging import getLogger
from os import walk, rename
from os.path import join, exists
from zipfile import ZipFile

from flask import send_file
from werkzeug.exceptions import NotFound

LOGGER = getLogger( __name__ )

class Resources( object ):

	def __init__( self, path, filter = None ):
		self.__resources = dict()
		if path.endswith( '.zip' ):
			LOGGER.info( 'Reading resources from zip file {0}'.format( path ) )
			with ZipFile( path, 'r' ) as zf:
				for entry in zf.namelist():
					if entry.endswith( '/' ) or ( filter and not filter( entry ) ): continue
					self.__resources[ entry ] = zf.read( entry )
		else:
			LOGGER.info( 'Reading resources from directory {0}'.format( path ) )
			lp = len( path )
			for dirname, dirs, files in walk( path ):
				for basename in files:
					full_path = join( dirname, basename )
					entry = full_path[ lp + 1: ]
					if filter and not filter( entry ): continue
					with open( full_path, 'r' ) as fp:
						self.__resources[ entry ] = fp.read()
	
	def entries( self ):
		return self.__resources.keys()
	
	def save( self, path, content ):
		self.__resources[ path ] = content
		return ''
		
	def load( self, path ):
		try:
			return self.__resources[ path ]
		except KeyError:
			return None
		
	def send( self, path, cache_timeout = None ):
		content = self.load( path )
		if content is None: raise NotFound
		return send_file( BytesIO( content ), attachment_filename = path, cache_timeout = cache_timeout )
	
	def dump( self, path ):
		if not path.endswith( '.zip' ): path += '.zip'
		if exists( path ): rename( path, path + '.old' )
		LOGGER.info( 'Saving resources to zip file {0}'.format( path ) )
		with ZipFile( path, 'w' ) as zf:
			for entry, content in self.__resources.items():
				zf.writestr( entry, content )

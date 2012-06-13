from io import BytesIO
from logging import getLogger
from os import walk
from os.path import join
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
		self.__resources[ path ] = content.encode( 'utf8' )
		return ''
		
	def load( self, path ):
		try:
			return self.__resources[ path ]
		except KeyError:
			return None
		
	def send( self, path ):
		content = self.load( path )
		if content is None: raise NotFound
		return send_file( BytesIO( content ), attachment_filename = path, cache_timeout = 1 )
	
	def dump( self, path ):
		with ZipFile( path, 'w' ) as zf:
			for entry, content in self.__resources.items():
				zf.writestr( entry, content )


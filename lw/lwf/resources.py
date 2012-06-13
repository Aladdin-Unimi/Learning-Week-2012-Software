from io import BytesIO
from logging import getLogger
from zipfile import ZipFile

from flask import send_file
from werkzeug.exceptions import NotFound

LOGGER = getLogger( __name__ )

class Resources( object ):

	def __init__( self, path, filter = None ):
		self.__resources = dict()
		with ZipFile( path, 'r' ) as zf:
			for entry in zf.namelist():
				if entry.endswith( '/' ) or ( filter and not filter( entry ) ): continue
				self.__resources[ entry ] = zf.read( entry )
	
	def entries( self ):
		return self.__resources.keys()
	
	def content( self, path ):
		try:
			return self.__resources[ path ]
		except KeyError:
			return None
		
	def send( self, path ):
		content = self.content( path )
		if content is None: raise NotFound
		return send_file( BytesIO( content ), attachment_filename = path )
	
	def dump( self, path ):
		with ZipFile( path, 'w' ) as zf:
			for entry, content in self.__resources.items():
				zf.writestr( entry, content )


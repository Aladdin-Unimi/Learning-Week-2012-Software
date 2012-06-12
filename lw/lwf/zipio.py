from logging import getLogger
from mimetypes import guess_type
from zipfile import ZipFile

LOGGER = getLogger( __name__ )

def load( path, filter = None ):
	result = dict()
	with ZipFile( path, 'r' ) as zf:
		for entry in zf.namelist():
			if entry.endswith( '/' ) or ( filter and not filter( entry ) ): continue
			mime_type, encoding = guess_type( entry )
			content = zf.read( entry )
			if mime_type and ( mime_type.startswith( 'text/' ) or mime_type == 'application/javascipt' ):
				try:
					content = content.decode( 'utf8' )	
				except UnicodeDecodeError:
					LOGGER.warn( 'Failed to decode {0}'.format( entry ) )
			result[ entry ] = content
	return result
	
def dump( dikt, path ):
	with ZipFile( path, 'w' ) as zf:
		for entry, content in dikt.items():
			zf.writestr( entry, content )
			

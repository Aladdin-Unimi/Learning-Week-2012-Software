from logging import getLogger
from zipfile import ZipFile

LOGGER = getLogger( __name__ )

def load( path, filter = None ):
	result = dict()
	with ZipFile( path, 'r' ) as zf:
		for entry in zf.namelist():
			if entry.endswith( '/' ) or ( filter and not filter( entry ) ): continue
			result[ entry ] = zf.read( entry )
	return result
	
def dump( dikt, path ):
	with ZipFile( path, 'w' ) as zf:
		for entry, content in dikt.items():
			zf.writestr( entry, content )


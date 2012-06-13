from logging import getLogger
from os.path import join, exists

from flask import send_file
from werkzeug.exceptions import NotFound

from . import BASE_PATH
from .resources import Resources

LOGGER = getLogger( __name__ )

def send_file_from_bytes( path, bytes ):
	return 

if BASE_PATH.endswith( '.zip' ):
    
	LOGGER.info( 'Serving assets from zip file {0}'.format( BASE_PATH ) )
	ASSETS = Resources( BASE_PATH, lambda entry: entry.startswith( 'assets/' ) )
	def assets( path ):
		return ASSETS.send( 'assets/{0}'.format( path ) )

else:

    BASE_DIR = join( BASE_PATH, 'assets' )
    LOGGER.info( 'Serving assets from filesystem dir {0}'.format( BASE_DIR ) )
    def assets( path ):
        ap = join( BASE_DIR, path )
        if exists( ap ):
            return send_file( open( ap, 'r' ) )
        else:
            raise NotFound

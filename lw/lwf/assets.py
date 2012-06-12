from logging import getLogger
from os.path import join, exists
from StringIO import StringIO

from flask import send_file
from werkzeug.exceptions import NotFound

from . import BASE_PATH
from .zipio import load

LOGGER = getLogger( __name__ )

if BASE_PATH.endswith( '.zip' ):
    
	LOGGER.info( 'Serving assets from zip file {0}'.format( BASE_PATH ) )
	ASSETS = load( BASE_PATH, lambda entry: entry.startswith( 'assets/' ) )
	def assets( path ):
		try:
			content = ASSETS[ path ]
		except KeyError:
			raise NotFound
		return send_file( StringIO( content ), attachment_filename = path )
else:

    BASE_DIR = join( BASE_PATH, 'assets' )
    LOGGER.info( 'Serving assets from filesystem dir {0}'.format( BASE_DIR ) )
    def assets( path ):
        ap = join( BASE_DIR, path )
        if exists( ap ):
            return send_file( open( ap, 'r' ) )
        else:
            raise NotFound

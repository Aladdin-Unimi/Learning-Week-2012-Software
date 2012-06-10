from logging import getLogger
from os.path import join, exists
from zipfile import ZipFile

from flask import send_file
from werkzeug.exceptions import NotFound

from . import BASE_PATH

LOGGER = getLogger( __name__ )

if BASE_PATH.endswith( '.zip' ):
    
    LOGGER.info( 'Serving assets from zip file {0}'.format( BASE_PATH ) )
    def assets( path ):
        with ZipFile( BASE_PATH, 'r' ) as zf:
            try:
                x = zf.open( join( 'assets', path ), 'r' )
            except KeyError:
                raise NotFound
            x.name = None
            return send_file( x, attachment_filename = path )
else:

    BASE_DIR = join( BASE_PATH, 'assets' )
    LOGGER.info( 'Serving assets from filesystem dir {0}'.format( BASE_DIR ) )
    def assets( path ):
        ap = join( BASE_DIR, path )
        if exists( ap ):
            return send_file( open( ap, 'r' ) )
        else:
            raise NotFound

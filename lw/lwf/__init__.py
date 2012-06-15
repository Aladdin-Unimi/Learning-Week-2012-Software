# setup logging

from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

LOGGER = getLogger( __name__ )
handler = StreamHandler()
handler.setLevel( DEBUG )
handler.setFormatter( Formatter( '127.0.0.1 - - [%(asctime)s] %(name)s: "%(message)s"','%Y/%b/%d %H:%M:%S' ) )
LOGGER.setLevel( DEBUG )
LOGGER.addHandler( handler )

# setup vendorized path (before we actually load libraries)

import sys
from os import getcwd
from os.path import join

BASE_PATH = join( getcwd(), sys.argv[ 0 ] )
sys.path.append( join( BASE_PATH, 'vendorized' ) )

# load resources from zip/filesystem

from .resources import Resources 

ASSETS = Resources( BASE_PATH, lambda entry: entry.startswith( 'assets/' ) )
USER_CODE = Resources( sys.argv[ 1 ] )
DATA = Resources( sys.argv[ 2 ] )
	
# setup the Flask application

from flask import Flask, render_template, request

app = Flask( __name__ )

# fix template loading so that it works also if code is loaded from a zip file

from jinja2 import PackageLoader, ChoiceLoader
from .apps import APPLICATIONS

loaders = [ PackageLoader( __name__ ) ] 
for prefix, blueprint in APPLICATIONS.items():
	app.register_blueprint( blueprint, url_prefix = '/{0}'.format( prefix ) )
	loaders.append( PackageLoader( 'lwf.apps.{0}'.format( prefix ) ) ) 
app.jinja_loader = ChoiceLoader( loaders ) # to find templates also if launched from zip

# define the basic routes of the main app

@app.route( '/' )
def index():
    return render_template( 'index.html' )

@app.route( '/misc' )
def misc():
    return render_template( 'misc.html' )


@app.route( '/shutdown' )
def shutdown():
	USER_CODE.dump( sys.argv[ 1 ] )
	sdf = request.environ.get( 'werkzeug.server.shutdown' )
	if sdf is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	sdf()
	return 'Arresto in corso...'

@app.route( '/assets/<path:path>' )
def assets( path ):
	return ASSETS.send( 'assets/{0}'.format( path ) )

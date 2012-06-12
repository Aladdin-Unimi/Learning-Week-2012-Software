import sys
from os import getcwd
from os.path import join

BASE_PATH = join( getcwd(), sys.argv[ 0 ] )
sys.path.append( join( BASE_PATH, 'vendorized' ) )

from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

LOGGER = getLogger( __name__ )
handler = StreamHandler()
handler.setLevel( DEBUG )
handler.setFormatter( Formatter( '127.0.0.1 - - [%(asctime)s] %(name)s: "%(message)s"','%Y/%b/%d %H:%M:%S' ) )
LOGGER.setLevel( DEBUG )
LOGGER.addHandler( handler )

from flask import Flask, render_template
from jinja2 import PackageLoader, ChoiceLoader

from .assets import assets

from .apps import APPLICATIONS

app = Flask( __name__ )

app.add_url_rule( '/assets/<path:path>', 'assets', assets ) # to serve assets from zip / filesystem

loaders = [ PackageLoader( __name__ ) ] 
for prefix, blueprint in APPLICATIONS.items():
	app.register_blueprint( blueprint, url_prefix = '/{0}'.format( prefix ) )
	loaders.append( PackageLoader( 'lwf.apps.{0}'.format( prefix ) ) ) 
app.jinja_loader = ChoiceLoader( loaders ) # to find templates also if launched from zip

@app.route('/')
def index():
    return render_template( 'index.html' )

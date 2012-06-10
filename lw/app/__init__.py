import sys
from os import getcwd
from os.path import join

BASE_PATH = join( getcwd(), sys.argv[ 0 ] )
sys.path.append( join( BASE_PATH, 'libs' ) )

from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

LOGGER = getLogger( __name__ )
handler = StreamHandler()
handler.setLevel( DEBUG )
handler.setFormatter( Formatter( '127.0.0.1 - - [%(asctime)s] %(name)s: "%(message)s"','%Y/%b/%d %H:%M:%S' ) )
LOGGER.setLevel( DEBUG )
LOGGER.addHandler( handler )

from flask import Flask, render_template
from jinja2 import PackageLoader

from .assets import assets

app = Flask( __name__ )
app.jinja_loader = PackageLoader( __name__ ) # to find templates also if launched from zip
app.add_url_rule( '/assets/<path:path>', 'assets', assets ) # to serve assets from zip / filesystem

@app.route('/')
def index():
    return render_template( 'index.html' )

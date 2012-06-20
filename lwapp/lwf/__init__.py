# Copyright (C) 2012 Massimo Santini <massimo.santini@unimi.it>
#
# This file is part of Learning-Week-2012-Software (lw12).
# 
# Learning-Week-2012-Software is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
# 
# Learning-Week-2012-Software is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the GNU General
# Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# Learning-Week-2012-Software If not, see <http://www.gnu.org/licenses/>.

# trying to follow http://semver.org/

__version__ = '0.4.0'

# setup vendorized path (before we actually load libraries)

import sys
from os import getcwd
from os.path import join

BASE_PATH = join( getcwd(), sys.argv[ 0 ] )
sys.path.append( join( BASE_PATH, 'vendorized' ) )

# setup the Flask application

from flask import Flask, render_template, request

app = Flask( __name__ )

# load resources from zip/filesystem

from .resources import Resources 

ASSETS = Resources( BASE_PATH, lambda entry: entry.startswith( 'assets/' ) )
USER_APPS = Resources( sys.argv[ 1 ] )
DATA = Resources( sys.argv[ 2 ] )
	
# fix template loading so that it works also if code is loaded from a zip file

from jinja2 import PackageLoader, ChoiceLoader
from .apps import APPLICATIONS
from .kml import metadata 

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
	USER_APPS.dump( sys.argv[ 1 ] )
	DATA.dump( sys.argv[ 2 ] )
	sdf = request.environ.get( 'werkzeug.server.shutdown' )
	if sdf is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	sdf()
	return 'Arresto in corso...'

@app.route( '/assets/<path:path>' )
def assets( path ):
	return ASSETS.send( 'assets/{0}'.format( path ) )

@app.route( '/favicon.ico' )
def favicon():
	return ASSETS.send( 'assets/img/favicon.ico' )

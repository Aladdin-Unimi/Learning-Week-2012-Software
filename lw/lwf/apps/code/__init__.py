from itertools import groupby

from flask import Blueprint, render_template, request
from werkzeug.exceptions import NotFound

from lwf import RESOURCES_PATH
from ...resources import Resources
from ...ycfg import read_configs

RESOURCES = Resources( RESOURCES_PATH )

APPLICATIONS_LIST = read_configs( RESOURCES.load( 'applications.yaml' ), '' )
APPLICATIONS = dict( ( ( _.name, _ ) for _ in APPLICATIONS_LIST ) )

code = Blueprint( 'code', __name__ )

@code.route( '/' )
def list():
	return render_template( 'list.html', applications = APPLICATIONS.values() )

@code.route( '/load/<path:path>' )
def load( path ):
	return RESOURCES.send( path )

@code.route( '/save/<path:path>', methods = [ 'POST' ] )
def save( path ):
	return RESOURCES.save( path, request.form[ 'content' ] )

@code.route( '/edit/<path:path>' )
def edit( path ):
	return render_template( 'edit.html', path = path )
	
@code.route( '/run/<name>' )
def run( name ):
	try:
		app = APPLICATIONS[ name ]
	except KeyError:
		raise NotFound
	return render_template( 'run.html', app = app )
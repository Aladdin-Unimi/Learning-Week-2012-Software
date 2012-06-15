from itertools import groupby

from flask import Blueprint, render_template, request, make_response
from werkzeug.exceptions import NotFound

from lwf import USER_CODE
from lwf.resources import Resources
from lwf.ycfg import read_configs

APPLICATIONS_LIST = read_configs( USER_CODE.load( 'applications.yaml' ), '' )
APPLICATIONS = dict( ( ( _.name, _ ) for _ in APPLICATIONS_LIST ) )

usr = Blueprint( 'usr', __name__ )

@usr.route( '/' )
def list():
	return render_template( 'list.html', applications = APPLICATIONS.values() )

@usr.route( '/load/<path:path>' )
def load( path ):
	response = make_response( USER_CODE.load( path ) ) # not using send method because don't work well with ace editor
	response.headers[ 'Content-type' ] = 'text/plain'
	return response

@usr.route( '/save/<path:path>', methods = [ 'POST' ] )
def save( path ):
	return USER_CODE.save( path, request.form[ 'content' ] )

@usr.route( '/edit/<path:path>' )
def edit( path ):
	return render_template( 'edit.html', path = path )
	
@usr.route( '/run/<name>' )
def run( name ):
	try:
		app = APPLICATIONS[ name ]
	except KeyError:
		raise NotFound
	return render_template( 'run.html', app = app )
from flask import Blueprint, render_template

from lwf import RESOURCES_PATH
from lwf.resources import Resources

RESOURCES = Resources( RESOURCES_PATH )

code = Blueprint( 'code', __name__ )

@code.route( '/' )
def list():
	return render_template( 'list.html', entries = RESOURCES.entries() )

@code.route( '/load/<path:path>' )
def load( path ):
	return RESOURCES.send( path )

@code.route( '/edit/<path:path>' )
def edit( path ):
	return render_template( 'edit.html', path = path )
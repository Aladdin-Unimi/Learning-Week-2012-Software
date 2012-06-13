from flask import Blueprint, render_template

from lwf import RESOURCES_PATH
from lwf.resources import Resources

RESOURCES = Resources( RESOURCES_PATH )

edit = Blueprint( 'edit', __name__ )

@edit.route( '/' )
def list():
	return render_template( 'list.html', entries = RESOURCES.entries() )

@edit.route( '/load/<path:path>' )
def res_load( path ):
	return RESOURCES.send( path )

@edit.route( '/<path:path>' )
def edit_path( path ):
	return render_template( 'editor.html', path = path )
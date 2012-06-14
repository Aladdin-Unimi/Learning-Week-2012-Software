from flask import Blueprint, render_template, make_response

from lwf import DATA

tag = Blueprint( 'tag', __name__ )

@tag.route( '/add' )
def index():
	return render_template( 'add.html' )
	
@tag.route( '/metadata' )
def metadata():
	response = make_response( DATA.load( 'metadata.kml' ) )
	response.headers[ 'Content-type' ] = 'application/vnd.google-earth.kml+xml'
	return response
from flask import Blueprint, render_template, make_response, request

from lwf import DATA

img = Blueprint( 'img', __name__ )

@img.route( '/add' )
def index():
	return render_template( 'add.html' )
	
@img.route( '/metadata' )
def metadata():
	response = make_response( DATA.load( 'metadata.kml' ) )
	response.headers[ 'Content-type' ] = 'application/vnd.google-earth.kml+xml'
	return response

@img.route( '/upload', methods = [ 'POST' ] )
def upload():
	x = len( request.files[ 'file' ].stream.read() )
	print x
	return str(x)

@img.route( '/get/<img>' )
def get( img ):
	return DATA.send( img )
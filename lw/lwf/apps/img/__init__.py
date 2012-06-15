from cgi import escape

from flask import Blueprint, render_template, make_response, request

from lwf import DATA
from lwf import kml

img = Blueprint( 'img', __name__ )

@img.route( '/add' )
def add():
	return render_template( 'add.html' )
	
@img.route( '/metadata' )
def metadata():
	response = make_response( DATA.load( 'metadata.kml' ) )
	response.headers[ 'Content-type' ] = 'application/vnd.google-earth.kml+xml'
	return response

@img.route( '/upload', methods = [ 'POST' ] )
def upload():
	data = request.form
	point = kml.point( float( data[ 'lat' ] ), float( data[ 'lon' ] ) )
	placemark = kml.placemark( point )
	placemark.appendChild( kml.name( data[ 'title' ].encode( 'utf8' ) ) )
	placemark.appendChild( kml.creator( data[ 'author' ].encode( 'utf8' ) ) )
	placemark.appendChild( kml.description( data[ 'description' ].encode( 'utf8' ) ) )
	kml.append( placemark )
	x = len( request.files[ 'file' ].stream.read() )
	return placemark.toprettyxml()

@img.route( '/get/<img>' )
def get( img ):
	return DATA.send( img )
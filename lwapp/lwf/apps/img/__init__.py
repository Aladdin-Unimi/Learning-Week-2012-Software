# Copyright (C) 2012 Massimo Santini <massimo.santini@unimi.it>
#
# This file is part of Learning-Week-2012-Software.
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

from cgi import escape

from flask import Blueprint, render_template, make_response, request

from lwf import DATA
from lwf import kml

img = Blueprint( 'img', __name__ )

kml.init( DATA.load( 'metadata.kml' ) )

@img.route( '/add' )
def add():
	return render_template( 'add.html' )
	
@img.route( '/metadata' )
def metadata():
	response = make_response( kml.metadata() )
	response.headers[ 'Content-type' ] = 'application/vnd.google-earth.kml+xml'
	return response

@img.route( '/upload', methods = [ 'POST' ] )
def upload():
	data = request.form
	try:
		lat, lon = float( data[ 'lat' ] ), float( data[ 'lon' ] )
	except ValueError:
		lat, lon = 0, 0
	placemark = kml.placemark( lat, lon  )
	placemark.appendChild( kml.name( data[ 'title' ] ) )
	placemark.appendChild( kml.creator( data[ 'author' ] ) )
	placemark.appendChild( kml.description( data[ 'description' ] ) )
	img = request.files[ 'file' ]
	img_id = kml.append( img.filename, placemark )
	DATA.save( img_id, img.stream.read() )
	DATA.save( 'metadata.kml', kml.metadata() )
	return placemark.toprettyxml( encoding = 'utf-8' )

@img.route( '/get/<img>' )
def get( img ):
	return DATA.send( img )
	
@img.route( '/list' )
def list():
	return render_template( 'imglist.html', imgs = kml.astuples()  )
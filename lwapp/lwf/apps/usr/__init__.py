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

from xml.dom.minidom import parseString, Node

from flask import Blueprint, render_template, request, make_response
from werkzeug.exceptions import NotFound

from lwf import USER_APPS
from lwf.resources import Resources

xml = parseString( USER_APPS.load( 'applications.xml' ) )

def g0fcd( e, tag ):
	t = e.getElementsByTagName( tag )
	if t: return ( tag, t[ 0 ].firstChild.data )
	else: return None

USER_APPS_DESC = []
for g in xml.getElementsByTagName( 'group' ):
	group_name = g0fcd( g, 'name' )[ 1 ]
	apps = []
	for a in g.getElementsByTagName( 'application' ):
		app = dict( ( g0fcd( a, 'name' ), ) )
		app.update( { 
			'code': [ c.firstChild.data for c in a.getElementsByTagName( 'code' ) ],
			'output': [ o.firstChild.data for o in a.getElementsByTagName( 'output' ) ],
			'input': [ dict( filter( None, ( g0fcd( i, t ) for t in ( 'name', 'type', 'desc', 'hint' ) ) ) ) for i in a.getElementsByTagName( 'input' ) ]
		} )
		apps.append( app )
	USER_APPS_DESC.append( ( group_name, apps ) )

usr = Blueprint( 'usr', __name__ )

@usr.route( '/' )
def list():
	return render_template( 'list.html', applications = USER_APPS_DESC )
	
@usr.route( '/load/<path:path>' )
def load( path ):
	return USER_APPS.send( path )

@usr.route( '/save/<path:path>', methods = [ 'POST' ] )
def save( path ):
	return USER_APPS.save( path, request.form[ 'content' ].encode( 'utf-8' ) )

@usr.route( '/edit/<path:path>' )
def edit( path ):
	return render_template( 'edit.html', path = path )
	
@usr.route( '/run/<int:group>/<int:application>' )
def run( group, application ):
	try:
		app = USER_APPS_DESC[ group ][ 1 ][ application ]
	except KeyError:
		raise NotFound
	return render_template( 'run.html', app = app )

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
	content = USER_CODE.load( path )
	if content is None: raise NotFound
	response = make_response( content ) # not using send method because don't work well with ace editor
	response.headers[ 'Content-type' ] = 'text/plain'
	return response

@usr.route( '/save/<path:path>', methods = [ 'POST' ] )
def save( path ):
	return USER_CODE.save( path, request.form[ 'content' ].encode( 'utf-8' ) )

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
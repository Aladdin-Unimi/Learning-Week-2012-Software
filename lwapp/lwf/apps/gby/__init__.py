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

from flask import Blueprint, render_template

gby = Blueprint( 'gby', __name__ )

@gby.route( '/language' )
def index():
	return render_template( 'language.html' )
	
@gby.route( '/maze' )
def maze():
	return render_template( 'maze.html' )

@gby.route( '/frame.html' )
def frame():
	return render_template( 'maze-frame.html' )

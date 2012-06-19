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

from logging import getLogger, FileHandler, StreamHandler, Formatter, DEBUG, INFO
from threading import Timer
from sys import argv, stderr
from webbrowser import open

LEVEL = INFO if argv[ 0 ].endswith( '.zip' ) else DEBUG

LOGGER = getLogger()
handler = StreamHandler() if LEVEL == DEBUG else FileHandler( 'lw12.log' )
handler.setLevel( LEVEL )
handler.setFormatter( Formatter( '127.0.0.1 - - [%(asctime)s] %(name)s: "%(message)s"','%Y/%b/%d %H:%M:%S' ) )
LOGGER.setLevel( LEVEL )
LOGGER.addHandler( handler )

from lwf import app

if __name__ == '__main__':
	if LEVEL == DEBUG:
		app.debug = True
	else:
		app.debug = False
		Timer( 3, lambda : open( 'http://localhost:5000/') ).start()
	app.run()

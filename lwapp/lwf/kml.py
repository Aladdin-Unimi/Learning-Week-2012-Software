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

from collections import namedtuple
from logging import getLogger
from os.path import splitext
from uuid import uuid1 as uuid
from xml.dom.minidom import Document, parseString

LOGGER = getLogger( __name__ )

Namespace = namedtuple( 'Namespace', 'uri prefix' )

TaggedImage = namedtuple( 'TaggedImage', 'path lat lon title author description')


NAMESPACES = {
	'kml': Namespace( 'http://www.opengis.net/kml/2.2', '' ),
	'foaf': Namespace( 'http://xmlns.com/foaf/0.1/', 'foaf' ),
	'dc': Namespace( 'http://dublincore.org/documents/dcmi-namespace/', 'dc' ),
	'xml': Namespace( 'http://www.w3.org/XML/1998/namespace', 'xml' ), 
}

doc = None

def init( metadata ):
	global doc
	if metadata is None:
		doc = Document()
		root = doc.createElementNS( NAMESPACES[ 'kml' ].uri, 'kml' )
		root.setAttribute( 'xmlns', NAMESPACES[ 'kml' ].uri )
		root.setAttribute( 'xmlns:' + NAMESPACES[ 'foaf' ].prefix, NAMESPACES[ 'foaf' ].uri )
		root.setAttribute( 'xmlns:' + NAMESPACES[ 'dc' ].prefix, NAMESPACES[ 'dc' ].uri )
		root.setAttribute( 'xmlns:' + NAMESPACES[ 'xml' ].prefix, NAMESPACES[ 'xml' ].uri )
		doc.appendChild( root )
	else:	
		doc = parseString( metadata )

def metadata():
	return doc.toxml( 'utf-8' )

def astuples():
	def x( pm, tag ):
		elem = pm.getElementsByTagName( tag )
		if not elem: return None
		fc = elem[ 0 ].firstChild;
		if not fc: return None
		return fc.nodeValue
	res = []
	for pm in doc.getElementsByTagName( 'Placemark' ):
		lat, lon = x( pm.getElementsByTagName( 'Point' )[ 0 ], 'coordinates' ).split( ',' )
		res.append( TaggedImage( 
			pm.attributes.getNamedItem( 'xml:id' ).value, lat, lon,
			x( pm, 'name' ), x( pm, 'dc:creator' ), x( pm, 'description' )
		) )
	return res
	
def append( img, placemark ):
	_, ext = splitext( img )
	img_id = uuid().hex + ext
	placemark.setAttributeNS( NAMESPACES[ 'xml' ].uri, '{0}:{1}'.format( NAMESPACES[ 'xml' ].prefix, 'id' ), img_id )
	doc.documentElement.appendChild( placemark )
	return img_id

def element( tagName, namespace = 'kml', child = None ):
	element = doc.createElementNS( 
		NAMESPACES[ namespace ].uri, 
		'{0}:{1}'.format( NAMESPACES[ namespace ].prefix, tagName ) if NAMESPACES[ namespace ].prefix else tagName 
	)
	if child: 
		if isinstance( child, unicode ): element.appendChild( doc.createTextNode( child ) )
		else: element.appendChild( child )
	return element

def placemark( lat, lon ):
	return element( 'Placemark', 
		child = element( 'Point', 
			child = element( 'coordinates', child = u'{0},{1}'.format( lat, lon ) ) 
		) 
	)

def creator( creator ):
	return element( 'creator', 'dc', creator )

def name( name ):
	return element( 'name', child = name )

def description( description ):
	return element( 'description', child = description )

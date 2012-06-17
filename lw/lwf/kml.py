from collections import namedtuple
from logging import getLogger
from os.path import splitext
from uuid import uuid1 as uuid
from xml.dom.minidom import Document, parseString

LOGGER = getLogger( __name__ )

Namespace = namedtuple( 'Namespace', 'uri prefix' )

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
		if isinstance( child, str ): element.appendChild( doc.createTextNode( child ) )
		else: element.appendChild( child )
	return element

def placemark( lat, lon ):
	return element( 'Placemark', 
		child = element( 'Point', 
			child = element( 'coordinates', child = '{0},{1}'.format( lat, lon ) ) 
		) 
	)

def creator( creator ):
	return element( 'creator', 'dc', creator )

def name( name ):
	return element( 'name', child = name )

def description( description ):
	return element( 'description', child = description )

from collections import namedtuple
from io import BytesIO
from logging import getLogger
from xml.dom.minidom import Document, parseString

LOGGER = getLogger( __name__ )

Point = namedtuple( 'Point', 'lat lon' )
Namespace = namedtuple( 'Namespace', 'uri prefix' )

NAMESPACES = {
	'kml': Namespace( 'http://www.opengis.net/kml/2.2', '' ),
	'foaf': Namespace( 'http://xmlns.com/foaf/0.1/', 'foaf' ),
	'dc': Namespace( 'http://dublincore.org/documents/dcmi-namespace/', 'dc' ),
	'xml': Namespace( 'http://www.w3.org/XML/1998/namespace', 'xml' ), 
}

def dump():
	resources.save_metadata( string() )

def string():
	return doc.toxml( 'utf-8' )
	
def append( placemark ):
	id = 'img_{0:03d}'.format( len( placemarks ) )
	placemark.setAttributeNS( NAMESPACES[ 'xml' ].uri, '{0}:{1}'.format( NAMESPACES[ 'xml' ].prefix, 'id' ), id )
	placemarks.append( placemark )
	doc.documentElement.appendChild( placemark )

def element( tagName, namespace = 'kml', child = None ):
	element = doc.createElementNS( 
		NAMESPACES[ namespace ].uri, 
		'{0}:{1}'.format( NAMESPACES[ namespace ].prefix, tagName ) if NAMESPACES[ namespace ].prefix else tagName 
	)
	if child: 
		if isinstance( child, str ): element.appendChild( doc.createTextNode( child ) )
		else: element.appendChild( child )
	return element

def placemark( point ):
	return element( 'Placemark', 
		child = element( 'Point', 
			child = element( 'coordinates', child = '{0},{1}'.format( point.lat, point.lon ) ) 
		) 
	)

def creator( creator ):
	return element( 'creator', 'dc', creator )

def name( name ):
	return element( 'name', child = name )

def description( description ):
	return element( 'description', child = description )
	
def point( lat, lon ):
	return Point( lat, lon )

doc = Document()
root = doc.createElementNS( NAMESPACES[ 'kml' ].uri, 'kml' )
root.setAttribute( 'xmlns', NAMESPACES[ 'kml' ].uri )
root.setAttribute( 'xmlns:' + NAMESPACES[ 'foaf' ].prefix, NAMESPACES[ 'foaf' ].uri )
root.setAttribute( 'xmlns:' + NAMESPACES[ 'dc' ].prefix, NAMESPACES[ 'dc' ].uri )
root.setAttribute( 'xmlns:' + NAMESPACES[ 'xml' ].prefix, NAMESPACES[ 'xml' ].uri )
doc.appendChild( root )

xml_placemarks = doc.getElementsByTagNameNS( NAMESPACES[ 'kml' ].uri, 'Placemark' )
placemarks = [ None ] * len( xml_placemarks )
for pm in xml_placemarks:
	id = pm.getAttributeNS( NAMESPACES[ 'xml' ].uri, 'id' )
	placemarks[ int( id.split( '_' )[ 1 ] ) ] = pm

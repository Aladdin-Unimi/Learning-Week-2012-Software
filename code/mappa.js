function init() {
	var metadata = loadMetadata();
	var points = metadata.getElementsByTagName('Point');
	for ( var i = 0; i < points.length ; i++ ) disegna( points[ i ] );
}

function estrai( point, tagname ) {
	var elem = point.parentNode.getElementsByTagName( tagname );
	if ( ! elem ) return undefined;
	var fc = elem[ 0 ].firstChild;
	if ( ! fc ) return undefined;
	return fc.nodeValue;
}

function disegna( point ) {
	var lat_lng = point.firstChild.firstChild.nodeValue.split( ',' );
	var title = estrai( point, 'name' );
	var description = estrai( point, 'description' );
	var src = '/img/' + parseInt( point.parentNode.attributes.getNamedItem( 'xml:id' ).value.split( '_' )[ 1 ] );
	marker( new Point( lat_lng[ 0 ], lat_lng[ 1 ] ), title, description, src );
}

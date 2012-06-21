function acaso( origine, raggio, n ) {

	function rnd( raggio ) {
		return Math.random() * 2 * raggio - raggio;
	}

	var markers = [];
	for ( var i = 0; i < n; i = i + 1 )
		markers.push( marker( [ origine[ 0 ] + rnd( raggio ),  origine[ 1 ] + rnd( raggio ) ] ) );
	return markers;
}

function m2r( marker ) {
	var pos = marker.getPosition();
	return [ pos.lng(), pos.lat() ];
}

function angolo( mo, ma, mb ) {
	var o = m2r( mo ), a = m2r( ma ), b = m2r( mb );
	return ( a[ 0 ] - o[ 0 ] ) * ( b[ 1 ] - o[ 1 ] ) - ( a[ 1 ] - o[ 1 ] ) * ( b[ 0 ] - o[ 0 ] );
}

function compara( ma, mb ) {
	var a = m2r( ma ), b = m2r( mb );
	if ( a < b ) return -1;
	if ( a == b ) return 0;
	return 1;
}

function numera( markers ) {
	for ( var i = 0; i < markers.length; i++ ) 
		number_marker( markers[ i ], i );
}

function poligono( markers ) {

	function m2p( marker ) {
		var pos = marker.getPosition();
		return [ pos.lat(), pos.lng() ];
	}

	var poligono = [];
	for ( var i = 0; i < markers.length; i = i + 1 )
		poligono.push( m2p( markers[ i ] ) );
	
	map.drawPolygon( {
		paths: poligono,
		strokeColor: '#BBD8E9',
		strokeOpacity: 1,
		strokeWeight: 3,
		fillColor: '#BBD8E9',
		fillOpacity: 0.6
	} );

}

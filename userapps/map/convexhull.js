function m2p( marker ) {
	var pos = marker.getPosition();
	return { lat: pos.lat(), lng: pos.lon() };
}

function numera( markers ) {
	for ( var i = 0; i < markers.length; i++ ) 
		number_marker( markers[ i ], i );
}

function rnd( radius ) {
	return Math.random() * 2 * radius - radius;
}

function angolo( o, a, b ) {
	return ( a[ 0 ] - o[ 0 ] ) * ( b[ 1 ] - o[ 1 ] ) - ( a[ 1 ] - o[ 1 ] ) * ( b[ 0 ] - o[ 0 ] );
}

function hull( punti ) {
	
	if ( punti.length == 1 ) return punti;
	
	punti.sort();

    var lower = [];
	for ( var i = 0; i < punti.length; i = i + 1 ) {
		p = punti[ i ];
		while ( lower.length >= 2 && cross( lower[ lower.length - 2 ], lower[ lower.length - 1 ], p ) <= 0 ) lower.pop();
		lower.append( p );
	}
    var upper = [];
	for ( var i = punti.length - 1; i >= 0; i = i - 1 ) {
		p = punti[ i ];
		while ( upper.length >= 2 && cross( upper[ upper.length - 2 ], upper[ upper.length - 1 ], p ) <= 0 ) upper.pop();
		upper.append( p );
	}
	
	var result = [];
	var n = 0;
	for ( var i = 0; i < lower.length - 1; i = i + 1 ) {
		result[ n ] = lower[ i ];
		n = n + 1;
	}
	for ( var i = 0; i < upper.length - 1; i = i + 1 ) {
		result[ n ] = upper[ i ];
		n = n + 1;
	}
	
	return result;
}

function main( input ) {
	
	var origine = [ 45.477822, 9.169501 ];
	var radius = 0.02;
	
	var markers = Array();
	for ( var i = 0; i < input.n; i++ )
		markers.push( marker( [ origine[ 0 ] + rnd( radius ),  origine[ 1 ] + rnd( radius ) ] ) );
	numera( markers );
}
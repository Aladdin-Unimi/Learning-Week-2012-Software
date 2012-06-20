var origine;

function distanza( p, q ) {
	return gcircle( p[ 0 ], p[ 1 ], q[ 0 ], q[ 1 ] );
}

function compara( x, y ) {
	var dx = distanza( origine, x );
	var dy = distanza( origine, y );
	if ( dx < dy ) return -1;
	if ( dx == dy ) return 0;
	return 1;
}

function main( input ){
	var posizioni = prendiPunti();
	origine = [ input.lat, input.lng ];
	var ordinate = merge_sort( posizioni );
	colloca( ordinate, input.n );
}

function prendiPunti() {
	var metadata = loadMetadata();
	var points = xpath( metadata, '//kml:Point/kml:coordinates/text()' );
	var latlng = Array();
	for ( var i = 0 ; i < points.length ; i++ ) {
		var ll = points[ i ].data.split( ',' );
		latlng[ i ] = [ parseFloat( ll[ 0 ] ), parseFloat( ll[ 1 ] ) ;
	}
	return latlng;
}

function colloca( a, n  ) {
	marker( origine, 'Punto ' + 0, 'Origine' );
	for( var i = 0 ; i < a.length && i < n ; i++ )
		number_marker( marker( a[ i ], 'Punto ' + ( i + 1 ), 'Distanza: ' + distanza( origine, a[ i ] ) ), i + 1 );
}
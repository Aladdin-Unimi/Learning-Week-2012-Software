function merge( a, b ) {
	var c = [];

	while ( a.length && b.length ) 
		if ( compara( a[ 0 ],  b[ 0 ] ) <= 0 ) metti( c, togli( a ) );
		else metti( c, togli( b ) );
	while ( a.length ) metti( c, togli( a ) );
	while ( b.length ) metti( c, togli( b ) );

	return c;
}

function main( input ) {
	var a = [ 1, 3, 5 ];
	var b = [ 2, 4, 6 ];
	output( merge( a, b ) );
}
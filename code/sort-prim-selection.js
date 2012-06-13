function indice_del_minimo( a, inizio ) {
	var im = inizio;
	for ( var i = inizio + 1; i < a.length; i++ )
		if ( compara( a[ im ], a[ i ] ) > 0 ) im = i;
	return im;
}

function main( input ) {
	var a = a_caso( 10, 0 );
	var i = indice_del_minimo( a, 0 );
	output( a );
	output( i + ", " + a[ i ] );
}
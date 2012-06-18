function indice_del_minimo( a, inizio ) {
	var im = inizio;
	for ( var i = inizio + 1; i < a.length; i++ )
		if ( compara( a[ im ], a[ i ] ) > 0 ) im = i;
	return im;
}

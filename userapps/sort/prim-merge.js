function merge( a, b ) {
	var c = [];

	while ( a.length && b.length ) 
		if ( compara( a[ 0 ],  b[ 0 ] ) <= 0 ) aggiungi_dietro( c, togli_davanti( a ) );
		else aggiungi_dietro( c, togli_davanti( b ) );
	while ( a.length ) aggiungi_dietro( c, togli_davanti( a ) );
	while ( b.length ) aggiungi_dietro( c, togli_davanti( b ) );

	return c;
}

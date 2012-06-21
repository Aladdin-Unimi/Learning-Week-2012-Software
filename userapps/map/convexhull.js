function convex_hull( markers ) {
	
	if ( markers.length == 1 ) return markers;
	
	ord = merge_sort( markers );
	
    var inf = [];
	for ( var i = 0; i < ord.length; i = i + 1 ) {
		while ( inf.length >= 2 && angolo( inf[ inf.length - 2 ], inf[ inf.length - 1 ], ord[ i ] ) <= 0 ) togli_dietro( inf );
		aggiungi_dietro( inf, ord[ i ] );
	}
    var sup = [];
	for ( var i = ord.length - 1; i >= 0; i = i - 1 ) {
		while ( sup.length >= 2 && angolo( sup[ sup.length - 2 ], sup[ sup.length - 1 ], ord[ i ] ) <= 0 ) togli_dietro( sup );
		aggiungi_dietro( sup, ord[ i ] );
	}
	
	var risultato = [];
	var n = 0;
	for ( var i = 0; i < inf.length - 1; i = i + 1 ) {
		risultato[ n ] = inf[ i ];
		n = n + 1;
	}
	for ( var i = 0; i < sup.length - 1; i = i + 1 ) {
		risultato[ n ] = sup[ i ];
		n = n + 1;
	}
	
	return risultato;
}

function main( input ) {
	
	var origine = [ 45.477822, 9.169501 ];
	var raggio = 0.02;
	
	var markers = acaso( origine, raggio, input.n );
	
	var risultato = convex_hull( markers );
	
	numera( risultato );

	poligono( risultato );
}
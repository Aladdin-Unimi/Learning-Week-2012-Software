function selection_sort( a ) {
	for ( var i = 0; i < a.length - 1; i++ )
		scambia( a, i, indice_del_minimo( a, i ) ); 
	return a;
}

function main( input ) {
	var a = a_caso( input.n );
	selection_sort( a );
	output( a );
}

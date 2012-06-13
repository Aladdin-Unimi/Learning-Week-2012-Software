function selection_sort( a ) {
	for ( var i = 0; i < a.length - 1; i++ )
		scambia( a, i, indice_del_minimo( a, i ) ); 
	return a;
}

function init() {
	input_ints( 1, 'numero di elementi' );
}

function main( input ) {
	var a = a_caso( input[ 0 ] );
	selection_sort( a );
	output( a );
}

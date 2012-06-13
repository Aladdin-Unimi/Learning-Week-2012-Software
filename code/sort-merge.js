function merge_sort( a ) {
	if ( a.length > 1 ) {
		var m = smezza( a );
		return merge( merge_sort( m[ 0 ] ), merge_sort( m[ 1 ] ) );
	} else return a;  
}

function init() {
	input_ints( 1, 'numero di elementi' );
}

function main( input ) {
	var a = a_caso( input[ 0 ], 0, 10 );
	var b = merge_sort( a );
	output( b );
}

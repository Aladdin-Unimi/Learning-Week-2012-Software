function merge_sort( a ) {
	if ( a.length > 1 ) {
		var m = smezza( a );
		return merge( merge_sort( m[ 0 ] ), merge_sort( m[ 1 ] ) );
	} else return a;  
}

function main( input ) {
	var a = a_caso( input.n );
	var b = merge_sort( a );
	output( b );
}

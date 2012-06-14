function bubble_sort( a ) {
	for ( var i = a.length; i > 1; i-- )
		for ( var j = 0; j < i - 1; j++ )
			if ( compara( a[ j ], a[ j + 1 ] ) > 0 ) scambia( a, j, j + 1 );
	return a;
}

function main( input ) {
	var a = a_caso( input.n );
	bubble_sort( a );
	output( a );
}

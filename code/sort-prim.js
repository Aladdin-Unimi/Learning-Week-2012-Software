var scambi;

function scambia( arr, i, j ) {
	scambi += 1;
	if ( i == j ) return;
	var t = arr[ i ];
	arr[ i ] = arr[ j ];
	arr[ j ] = t;
}

var confronti;

function compara( x, y ) {
	confronti += 1;
	if ( x < y ) return -1;
	if ( x == y ) return 0;
	return 1;
}

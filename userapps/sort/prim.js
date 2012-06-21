function a_caso( n, min, max ) {
	var res = [];
	if ( min === undefined ) min = 0;
	if ( max === undefined ) max = n * n;
	for ( var i = 0; i < n; i++ ) res.push( Math.floor( Math.random() * ( max - min ) + min ) );
	return res;  
}

function ordinato( a ) {
	for ( var i = 0; i < a.length - 1; i++ )
		if ( a[ i ] > a[ i + 1 ] ) return false;
	return true;
}

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

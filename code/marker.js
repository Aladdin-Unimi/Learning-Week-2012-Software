function init() {
	input_floats( 2, [ 'latitudine', 'longitudine' ] );
	output( 'Prova con le coordinate: 45.477822, 9.169501' );
}

function main( input ) {
	var p = new Point( input[ 0 ], input[ 1 ] );
	marker( p );
}

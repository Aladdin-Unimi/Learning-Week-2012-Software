function init() {
	input_ints( 1, 'Numero di punti' );
}

function main( input ) {
	var data = table( 'x', [ 'retta', 'parabola' ] );
	for ( var i = 0; i < input[ 0 ]; i++ ) data.addRow( [ "" + i, i, i * i ] );
	draw( data );
}

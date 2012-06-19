function main( input ) {
	var data = table( 'x', [ 'retta', 'parabola' ] );
	for ( var i = 0; i < input.n; i++ ) data.addRow( [ "" + i, i, i * i ] );
	draw( data );
}

function mostra( punti ) {
	for ( var i = 0; i < punti.length; i++ ) 
		number_marker( marker( punti[ i ] ), i );
}

function rnd( radius ) {
	return Math.random() * 2 * radius - radius;
}

function main( input ) {
	
	var origine = [ 45.477822, 9.169501 ];
	var radius = 0.02;
	
	var punti = Array();
	punti.push( origine );
	for ( var i = 0; i < input.n; i++ ) {
		punti.push( [ origine[ 0 ] + rnd( radius ), origine[ 1 ] + rnd( radius ) ] );
	}
	mostra( punti );
}
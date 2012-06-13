function init() {
	input_ints( 2, [ 'primo addendo', 'secondo addendo' ] );
	input_strings( 2, [ 'prima parola', 'seconda parola' ] );
}

function main( input ) {
	output( input[ 0 ] + input[ 1 ] );
	output( input[ 2 ] + input[ 3 ] );
}

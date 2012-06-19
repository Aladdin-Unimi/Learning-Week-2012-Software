function color() {
	var color = [ 'red', 'green', 'blue' ];
	return color[ Math.floor( Math.random() * 3 ) ];
}

function main( input ) {
	output( color() );
}

function init() {
	input_strings( 1,'query' );
	output( 'Prova con: "//kml:Placemark/dc:creator" (senza virgolette)' );
}

function main( input ) {
	var d = loadMetadata();
	var r = xpath( d, input[ 0 ] );
	output( '' + serialize( r ) );
}

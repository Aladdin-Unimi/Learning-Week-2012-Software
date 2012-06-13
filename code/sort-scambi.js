function init() {
	input_ints( 1, 'numero di prove' );
}

function main( input ) {
	var data = table( 'N', [ 'selection', 'bubble' ] );
	
	var len = 0;
	
	var a, scambi_merge, scambi_selection, scambi_bubble;
	
	for ( var prove = input[ 0 ]; prove; prove-- ) {
		
		len += 100;
		
		a = a_caso( len );
		scambi = 0;
		selection_sort( a );
		scambi_selection = scambi;

		a = a_caso( len );
		scambi = 0;
		bubble_sort( a );
		scambi_bubble = scambi;
		
		data.addRow( [  "" + len, scambi_selection, scambi_bubble ] );
	}
	
	draw( data );
}

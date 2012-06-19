function main( input ) {
	var data = table( 'N', [ 'merge', 'selection', 'bubble' ] );
		
	var len = 0;
	
	var a, scambi_merge, scambi_selection, scambi_bubble;
	
	for ( var prove = input.n; prove; prove-- ) {
		
		len += 100;

		a = a_caso( len );
		scambi = 0;
		merge_sort( a );
		scambi_merge = scambi;

		a = a_caso( len );
		scambi = 0;
		selection_sort( a );
		scambi_selection = scambi;

		a = a_caso( len );
		scambi = 0;
		bubble_sort( a );
		scambi_bubble = scambi;
		
		data.addRow( [  "" + len, scambi_merge, scambi_selection, scambi_bubble ] );
	}
	
	draw( data );
}

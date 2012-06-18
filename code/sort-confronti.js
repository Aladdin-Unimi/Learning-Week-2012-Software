function main( input ) {
	var data = table( 'N', [ 'merge', 'selection', 'bubble' ] );
	
	var len = 0;
	
	var a, confronti_merge, confronti_selection, confronti_bubble;
	
	for ( var prove = input.n; prove; prove-- ) {
		
		len += 100;
		
		a = a_caso( len );
		confronti = 0;
		merge_sort( a );
		confronti_merge = confronti;

		a = a_caso( len );
		confronti = 0;
		selection_sort( a );
		confronti_selection = confronti;

		a = a_caso( len );
		confronti = 0;
		bubble_sort( a );
		confronti_bubble = confronti;
		
		data.addRow( [  "" + len, confronti_merge, confronti_selection, confronti_bubble ] );
	}
	
	draw( data );
}

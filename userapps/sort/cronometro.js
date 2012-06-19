function main( input ) {
	var data = table( 'N', [ 'merge', 'selection', 'bubble' ] );
	
	var len = 0;
	
	var a, millisecondi_merge, millisecondi_selection, millisecondi_bubble;
	
	for ( var prove = input.n; prove; prove-- ) {
		
		len += 100;
		
		a = a_caso( len );
		millisecondi_merge = millisecondi();
		merge_sort( a );
		millisecondi_merge = millisecondi() - millisecondi_merge;

		a = a_caso( len );
		millisecondi_selection = millisecondi();
		selection_sort( a );
		millisecondi_selection = millisecondi() - millisecondi_selection;

		a = a_caso( len );
		millisecondi_bubble = millisecondi();
		bubble_sort( a );
		millisecondi_bubble = millisecondi() - millisecondi_bubble;
		
		data.addRow( [  "" + len, millisecondi_merge, millisecondi_selection, millisecondi_bubble ] );
	}
	
	draw( data );
}

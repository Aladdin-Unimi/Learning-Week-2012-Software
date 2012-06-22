function main( input ) {
	output( "Secondo Alice, il numero da usare è:" 
	    + diffie(input.n, input.p, input.x) );
	output( "Secondo Bruno, il numero da usare è:" 
	    + diffie(input.n, input.p, input.y) );

	output( "Il numero segreto condiviso è (secondo A):....");
	output( "Il numero segreto condiviso è (secondo B):....");

}

function diffie( n, p, r ){
  // da implementare
}

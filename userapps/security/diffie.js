function main( input ) {
	output( "Secondo Alice, il segreto condiviso è:" 
	    + diffie(input.n, input.p, input.x) );
	output( "Secondo Bruno, il segreto condiviso è:" 
	    + diffie(input.n, input.p, input.y) );
}

function diffie( n, p, r ){
  // da implementare
}

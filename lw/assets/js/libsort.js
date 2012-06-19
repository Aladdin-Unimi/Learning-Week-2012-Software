/*
	Copyright (C) 2012 Massimo Santini <massimo.santini@unimi.it>

	This file is part of Learning-Week-2012-Software.

	Learning-Week-2012-Software is free software: you can redistribute it and/or
	modify it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or (at your
	option) any later version.

	Learning-Week-2012-Software is distributed in the hope that it will be
	useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the GNU General
	Public License for more details.

	You should have received a copy of the GNU General Public License along with
	Learning-Week-2012-Software If not, see <http://www.gnu.org/licenses/>.
*/

function millisecondi() {
	return (new Date).getTime();
}

function a_caso( n, min, max ) {
	var res = [];
	if ( min === undefined ) min = 0;
	if ( max === undefined ) max = n * n;
	for ( var i = 0; i < n; i++ ) res.push( Math.floor( Math.random() * ( max - min ) + min ) );
	return res;  
}

function ordinato( a ) {
	for ( var i = 0; i < a.length - 1; i++ )
		if ( a[ i ] > a[ i + 1 ] ) return false;
	return true;
}

function metti( arr, elem ) {
	arr.push( elem );
}

function togli( arr, idx ) {
	if ( idx === undefined ) return arr.shift();
	else 
	var val = arr.splice( idx, 1 );
	return val[ 0 ];
}

function smezza( arr ) {
	return [ arr.slice( 0, arr.length / 2 ), arr.slice( arr.length / 2, arr.length ) ];
}

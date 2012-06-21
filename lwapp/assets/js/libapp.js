/*
	Copyright (C) 2012 Massimo Santini <massimo.santini@unimi.it>, Mattia Monga <mattia.monga@unimi.it>

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

/* text */

function output( str, label ) {
    $( "#output" ).append( "<p>" + ( label === undefined ? '' : label ) + str +"</p>" );
}

/* map */ 

var map = null; // after _init_map this will be instantiated as a google.maps.Map

function _init_map( lat, lng ) {
	if ( typeof google == 'undefined' || typeof google.maps == 'undefined' ) return;
	if ( lat === undefined ) {
		lat = 45.477822;
		lng = 9.169501;
	}
	map = new GMaps( {
		div: $( '#map' ), 
		lat: lat,
		lng: lng,
		zoom: 13,
		type: 'Roadmap',
		disableDefaultUI: true
	} );
}

function number_marker( marker, num ) {
	var icon = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=" + num + "|00ffff|000000";
	marker.setIcon( icon );
}

function marker( point, title, description, img, extra ) {
	if ( ! map ) return;
	if ( title === undefined ) title = '';
	var options =  {
		lat: point[ 0 ],
		lng: point[ 1 ],
		title: title,	 
	};
	if ( description !== undefined ) {
		var content = "<h3>" + title + "</h3><p>" + description + "</p>";
		if ( img !== undefined )
			content += "<img src='" + img + "' height=100 width=100/>";
		if ( extra !== undefined )
			content += extra;
		options[ 'infoWindow' ] = { content: content };
	}
	var marker = map.addMarker( options );
	return marker;
}

/* chart */

function table( absicssa, ordinates ) {
	var table = new google.visualization.DataTable();
	table.addColumn( 'string', absicssa );
	for ( var i = 0; i < ordinates.length; i++ )
		table.addColumn( 'number', ordinates[ i ] );
	return table;
}

function draw( data ) {
	var chart = new google.visualization.LineChart( document.getElementById( 'chart' ) );
	chart.draw( data, { curveType: 'none', width: 800, height: 400 } );
}

/* xml / xpath */

function loadMetadata() {
	var xhttp = new XMLHttpRequest();
	xhttp.open( 'GET', '/img/metadata', false );
	xhttp.send( '' );
	return xhttp.responseXML;
}

function KMLnsResolver( prefix ) {  
	var ns = {  
		'xml': 'http://www.w3.org/XML/1998/namespace',
		'kml': 'http://www.opengis.net/kml/2.2',
		'dc': 'http://dublincore.org/documents/dcmi-namespace/',
		'foaf': 'http://xmlns.com/foaf/0.1/',
		'xhtml' : 'http://www.w3.org/1999/xhtml',
	};  
	return ns[ prefix ] || null;
}  

function xpath( data, query ) {
	var eval_res = data.evaluate( query, data.documentElement, KMLnsResolver, XPathResult.ANY_TYPE, null );
	var res = Array();
	var i;
	while ( i = eval_res.iterateNext() ) res.push( i );
	return res;
}

var _serializer = new XMLSerializer();

function serialize( res ) {
	if ( ! ( res instanceof Array ) ) return _serializer.serializeToString( res );
	var str = Array();
	for ( var i = 0; i < res.length; i++ ) str.push( _serializer.serializeToString( res[ i ] ) );
	return str;
}

/* method called by run button */

function _run() {
	var input = Object();
	var inputs = document.getElementsByTagName( 'input' );
	for ( i = 0; i < inputs.length; i++ ) {
		var name = inputs[ i ].id;
	    if ( inputs[ i ].dataset[ 'type '] == 'int' ) input[ name ] = parseInt( inputs[ i ].value );
		else if ( inputs[ i ].dataset[ 'type' ] == 'float' ) input[ name ] = parseFloat( inputs[ i ].value );
		else input[ name ] = inputs[ i ].value;
	}
	$( "#output" ).html( "" );
	_init_map();
	main( input );
}

/* array helpers */

function aggiungi_dietro( arr, elem ) {
	arr.push( elem );
}

function togli_davanti( arr ) {
	return arr.shift();
}

function togli_dietro( arr ) {
	return arr.pop();
}

function smezza( arr ) {
	return [ arr.slice( 0, arr.length / 2 ), arr.slice( arr.length / 2, arr.length ) ];
}

/* misc */

function millisecondi() {
	return (new Date).getTime();
}
 
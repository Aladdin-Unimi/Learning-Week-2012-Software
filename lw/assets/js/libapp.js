/*
	Copyright (C) 2010 Massimo Santini, Mattia Monga

	This file is part of lw09-dico-dsi.
	lw09-dico-dsi is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	lw09-dico-dsi is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with lw09-dico-dsi.  If not, see <http://www.gnu.org/licenses/>.
*/

var map = null; // after _init_map this will be instantiated as a google.maps.Map
var Point = null; // after _init_map this will be google.maps.LatLng
var Table = null; // after _init_chart this will be instantiatend as a google.visualization.DataTable
var DEBUG; // if true, fvlogger will be enabled 

/**
	Sest the style of the element with the given id to 'block'
*/
function _show( id ) {
	var element = document.getElementById( id );
	if ( element ) element.style.display = 'block';
}

/**
	Inits the Google map object (and Point function) after makeing the 
	fieldsef of id 'mapfs' (that contains the map div) visible.
*/
function _init_map( lat, lng ) {
	if ( map ) return;
	if ( typeof google.maps == 'undefined' ) return;
	if ( lat === undefined ) {
		lat = 45.477822;
		lng = 9.169501;
	}
	_show( 'mapfs' );
	map = new google.maps.Map( document.getElementById( 'map' ), {
		zoom: 13,
		center: new google.maps.LatLng( lat, lng ),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	} );
	Point = google.maps.LatLng;
}

function _init_chart() {
	if ( typeof google.visualization == 'undefined' ) return;
	_show( 'chartfs' );
}

/**
	If the google object is defined, it initializes the map and then calls the user init function.
*/
function _init() {
	if ( typeof google != 'undefined' ) {
		_init_map();
		_init_chart();
	}
	if ( DEBUG ) _show( 'fvlogger' );
}

/**
	Called by 'onclick' by the button in the input fieldset, collects inputs and passes them
	to the user main function.
*/
function _main() {
	var input = Object();
	var inputs = document.getElementsByTagName( 'input' );
	for ( i = 0; i < inputs.length; i++ ) {
		var name = inputs[ i ].id;
	    if ( inputs[ i ].dataset[ 'type '] == 'int' ) input[ name ] = parseInt( inputs[ i ].value );
		else if ( inputs[ i ].dataset[ 'type' ] == 'float' ) input[ name ] = parseFloat( inputs[ i ].value );
		else input[ name ] = inputs[ i ].value;
	}
	$( "#output" ).html( "" );
	if ( DEBUG ) eraseLog( false );
	// if map and chart are defined we should re-init them!
	if ( DEBUG ) try {
		main( input );
	} catch ( err ) {
		error( err );
	} else main( input );
}

function output( str, label ) {
    $( "#output" ).append( "<p>" + ( label === undefined ? '' : label ) + str +"</p>" );
}

/* Google Map primitives */ 

function number_marker( marker, num ) {
	var icon = "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=" + num + "|00ffff|000000";
	marker.setIcon( icon );
}

function marker( point, title, description, src, extra ) {
	if ( ! map ) return;
	if ( title === undefined ) title = '';
	var marker = new google.maps.Marker( { position: point, map: map, title: title } );
	if ( description !== undefined ) {
		var content = "<h3>" + title + "</h3><p>" + description + "</p>";
		if ( src !== undefined )
			content += "<img src='" + src + "' height=100 width=100/>";
		if ( extra !== undefined )
			content += extra;
		var infowindow = new google.maps.InfoWindow( { content: "<div>" + content + "</div>" } );
		google.maps.event.addListener( marker, 'click', function() {
			infowindow.open( map, marker );
		} );
	}
	return marker;
}

/* Google Chart primitives */

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

/**
	Returns images metadata as an XML DOM element.
*/
function loadMetadata() {
	var xhttp = new XMLHttpRequest();
	xhttp.open( 'GET', '/img/metadata', false );
	xhttp.send( '' );
	return xhttp.responseXML;
}

/* A few xpath helpers */

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

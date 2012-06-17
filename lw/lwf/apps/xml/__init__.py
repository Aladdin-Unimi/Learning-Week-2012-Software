from flask import Blueprint, render_template, make_response, request

xml = Blueprint( 'xml', __name__ )

@xml.route( '/' )
def playground():
	return render_template( 'playground.html' )

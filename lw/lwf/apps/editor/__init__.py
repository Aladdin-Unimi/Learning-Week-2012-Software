from flask import Blueprint, render_template

editor = Blueprint( 'editor', __name__ )

@editor.route( '/edit/<path:path>')
def edit( path ):
	return render_template( 'editor.html' )
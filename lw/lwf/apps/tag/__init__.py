from flask import Blueprint, render_template

tag = Blueprint( 'tag', __name__ )

@tag.route( '/add' )
def index():
	return render_template( 'add.html' )
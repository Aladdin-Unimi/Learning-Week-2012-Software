from flask import Blueprint, render_template

test = Blueprint( 'test', __name__ )

@test.route( '/' )
def index():
	return render_template( 'test.html' )
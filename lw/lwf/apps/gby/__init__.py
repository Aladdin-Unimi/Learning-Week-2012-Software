from flask import Blueprint, render_template

gby = Blueprint( 'gby', __name__ )

@gby.route( '/language' )
def index():
	return render_template( 'language.html' )
	
@gby.route( '/maze' )
def maze():
	return render_template( 'maze.html' )

@gby.route( '/frame.html' )
def frame():
	return render_template( 'maze-frame.html' )

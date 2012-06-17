from json import load, dump, dumps
from getpass import getpass
from mimetypes import guess_type
from os.path import expanduser, exists, getsize, basename
from subprocess import check_output
from sys import argv 

from requests import post, delete

_, user, repo, path, desc = argv

tokens_path = expanduser( '~/.dmtokens' )
if exists( tokens_path ):
	with open( tokens_path, 'r' ) as f:
		tokens = load( f )
else:
	tokens = dict()

if not user in tokens:		
	pwd = getpass()
	data = { "scopes": [ "user", "repo" ], "note": "Download Manager" }
	r = post( 'https://api.github.com/authorizations', auth = ( user, pwd ), data = dumps( data ) )
	token = tokens[ user ] = r.json[ 'token' ]
	with open( tokens_path, 'w' ) as f:
		dump( tokens, f )
else:
	token = tokens[ user ]
	name = basename( path )
	content_type = guess_type( path )[ 0 ]
	headers = { 'Authorization': 'token {0}'.format( token ) }
	data = { "name": name, "size": getsize( path ), "description": desc, "content_type": content_type }
	r = post( 'https://api.github.com/repos/{0}/{1}/downloads'.format( user, repo ), data = dumps( data ), headers = headers )
	r = r.json
	# files = { 'file': ( name, open( path, 'rb') ) }
	# data = { 
	# 	'key': 'downloads/{0}/{1}/{2}'.format( user, repo, name ),
	# 	'acl': 'private',
	# 	'success_action_status': '201',
	# 	'Filename': name,
	# 	'AWSAccessKeyId': r[ 'accesskeyid' ],
	# 	'Policy': r[ 'policy' ],
	# 	'Signature': r[ 'signature' ],
	# 	'Content-Type': content_type
	# }	
	cmd = [
		'curl',
		'-F', 'key=downloads/{0}/{1}/{2}'.format( user, repo, name ), 
		'-F', 'acl=private',
		'-F', 'success_action_status=201',
		'-F', 'Filename={0}'.format( name ),
		'-F', 'AWSAccessKeyId={0}'.format( r[ 'accesskeyid' ] ),
		'-F', 'Policy={0}'.format( r[ 'policy' ] ),
		'-F', 'Signature={0}'.format( r[ 'signature' ] ),
		'-F', 'Content-Type={0}'.format( content_type ),
		'-F', 'file=@{0}'.format( path ),
		'https://github.s3.amazonaws.com/'
	]
	print check_output( cmd )
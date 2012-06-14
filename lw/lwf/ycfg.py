import yaml

class Dao( object ):
	
	def __init__( self, dikt, default = None ):
		self.__dikt = dikt
		self.default = default
	
	def __getattr__( self, attr ):
		try:
			return self.__dikt[ attr ]
		except KeyError:
			if self.default is not None: return self.default
			else: raise

	def keys( self ):
		return self.__dikt.keys()

	@staticmethod
	def daoize( data, default = None ):
		if isinstance( data, dict ):
			return Dao( data, default )
		elif isinstance( data, list ):
			return [ Dao.daoize( _, default ) for _ in data ]

def read_configs( yaml_string, default = None ):
	return Dao.daoize( yaml.load( yaml_string ), default )


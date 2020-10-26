class ModelException(Exception):
	"""docstring for ModelException"""
	
	exceptions = {'KeyError': "Sequence is not complete"}

	def __init__(self, error_name):
		super(ModelException, self).__init__(self.exceptions.get(error_name))
		
		
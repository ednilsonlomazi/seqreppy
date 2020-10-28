class ModelExc(Exception):
	"""docstring for ModelExc"""
	
	exceptions = {'KeyError': "Sequence is not complete"}

	def __init__(self, error_name):
		super(ModelExc, self).__init__(self.exceptions.get(error_name))
		
		
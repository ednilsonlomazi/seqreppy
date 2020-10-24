class ModelException(Exception):
	"""docstring for ModelException"""
	
	exceptions = {0: "Sequence must be a DNA type and complete"}

	def __init__(self, exc_id):
		super(ModelException, self).__init__(self.exceptions.get(exc_id))
		
		
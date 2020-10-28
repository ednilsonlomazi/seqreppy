class DataException(Exception):
	"""docstring for DataException"""
	
	exceptions = {"IndexError": "File is not at fasta format"}

	def __init__(self, error_name):
		super(DataException, self).__init__(self.exceptions.get(error_name))
		
		
class DataExc(Exception):
	"""docstring for DataExc"""
	
	exceptions = {"IndexError": "File is not at fasta format"}

	def __init__(self, error_name):
		super(DataExc, self).__init__(self.exceptions.get(error_name))
		
		
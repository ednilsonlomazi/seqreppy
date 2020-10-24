class DataException(Exception):
	"""docstring for DataException"""
	
	exceptions = {0: "Sequence is not an RNA", 1: "Sequence is not complete", 2: "File is not at fasta format"}

	def __init__(self, exc_id):
		super(DataException, self).__init__(self.exceptions.get(exc_id))
		
		
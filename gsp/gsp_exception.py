class GspExc(Exception):
	"""docstring for GspExc"""
	
	exceptions = {0: "This numerical dna representation is not frequently used on Power Spectrum. Please, try another"}

	def __init__(self, exc_id):
		super(GspExc, self).__init__(self.exceptions.get(exc_id))
		
		
class EncoderException(Exception):
	"""docstring for EncoderException"""
	
	exceptions = {"KeyError": {0: " was not indicated for perform coding"},
				  "IndexError": {0: " sequence identification do not exist"},
				  "Exception": {0: " is not present on Seqreppy models", 1: " has no graphical representation. Try: gsp=True", 2: ' Results are not in gsp. Try: gsp=True on perform_encoding function'}}

	def build_message(self, exc_id, info, exc_name):
		return ''.join((info, self.exceptions[exc_name][exc_id]))

	def __init__(self, exc_id, info, exc_name="Exception"):
		super(EncoderException, self).__init__(self.build_message(exc_id, info, exc_name))
		
		
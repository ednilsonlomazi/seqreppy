class EncoderException(Exception):
	"""docstring for EncoderException"""
	
	exceptions = {0: " is not present on DnaNR models", 1: " was not indicated", 2: " has no graphical representation. Try: gsp=True"}

	def build_message(self, exc_id, signature):
		return signature + self.exceptions.get(exc_id)

	def __init__(self, exc_id, signature):
		super(EncoderException, self).__init__(self.build_message(exc_id, signature))
		
		
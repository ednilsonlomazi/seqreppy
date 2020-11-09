import seqreppy.model.model as md

class Integer(md.Model):
	"""
	P. D. Cristea, “Genetic signal representation and analysis,” in Proc. of
	Society of Photo-Optical Instrumentation Engineers (SPIE) conference,
	vol. 4623, January 2002, pp. 77-84.
	"""
	signature = "Integer"

	def __init__(self):
		self.integers = {'A': 2, 'T': 0, 'C': 1, 'G': 3}

	def get_integer_value(self, base): return self.integers[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_integer_value, raw_sequence)))
		except Exception as e: raise md.ModelExc(type(e).__name__)

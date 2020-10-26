import seqreppy.models.model as md

class Integer(md.Model):
	"""
	Cristea, P. D. (2002). Conversion of nucleotides sequences into genomic signals. Journal of cellular and molecular medicine, 6(2), 279-303.
	"""
	signature = "Integer"

	def __init__(self):
		self.integers = {'A': 2, 'T': 0, 'C': 1, 'G': 3}

	def get_integer_value(self, base): return self.integers[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_integer_value, raw_sequence)))
		except Exception as e: raise md.ModelException(type(e).__name__)

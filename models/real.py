import seqreppy.models.model as md

class Real(md.Model):
	"""
	Chakravarthy, N., Spanias, A., Iasemidis, L. D., & Tsakalis, K. (2004). Autoregressive modeling and feature analysis of DNA sequences. EURASIP Journal on Advances in Signal Processing, 2004(1), 952689.
	"""
	signature = "Real"

	def __init__(self):
		self.real_numbers = {'A': -1.5, 'T': 1.5, 'C': 0.5, 'G': -0.5}

	def get_real_numbers(self, base): return self.real_numbers.get(base) 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_real_numbers, raw_sequence)))	
		except Exception: raise md.ModelException(0)
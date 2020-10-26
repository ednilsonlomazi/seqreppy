import seqreppy.models.model as md

class Complex(md.Model):
	"""D. Anastassiou, “Genomic signal processing,” IEEE Signal Processing
		Magazine, vol. 18, pp. 8-20, July 2001."""
	
	signature = "Complex"

	def __init__(self):
		self.complex_numbers = {'A': complex(1, 1), 'T': complex(1, -1), 'C': complex(-1, 1), 'G': complex(-1, -1)}

	def get_complex_number(self, base): return self.complex_numbers[base]
			
	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_complex_number, raw_sequence)), dtype=md.np.complex64)
		except Exception as e: raise md.ModelException(type(e).__name__)
import seqreppy.models.model as md

class Voss(md.Model):
	""" Voss, R. F. (1992) “Evolution of Long-range Fractal Correlations and 1/f noise in DNA
		base sequences”, Physical Review Leters, v. 68, p. 3805-3808."""

	signature = "Voss"

	def __init__(self):
		self.bin_indicators = {'A': (1,0,0,0), 'T': (0,1,0,0), 'C': (0,0,1,0), 'G': (0,0,0,1)}

	def get_bin_indicator(self, base): return self.bin_indicators.get(base)
		 		
	def encode_one(self, raw_sequence):
		try: return md.np.transpose(md.np.array(tuple(map(self.get_bin_indicator, raw_sequence))))
		except Exception: raise md.ModelException(0)

import seqreppy.models.model as md

class PairedNumericMapping(md.Model):
	""" Akhtar, M., Epps, J., Ambikairajah, E. (2007) “On DNA numerical representations for
		period-3 based exon prediction”, In: 2007 IEEE international workshop on genomic
		signal processing and statistics, IEEE, p. 1-4."""

	signature = "PairedNumericMapping"

	def __init__(self):
		self.pnumbers = {'A': 1, 'T': 1, 'C': -1, 'G': -1}

	def get_pn(self, base): return self.pnumbers[base] 
		
	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_pn, raw_sequence)))
		except Exception as e: raise md.ModelException(type(e).__name__)
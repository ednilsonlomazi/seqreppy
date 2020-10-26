import seqreppy.models.model as md 

class DnaWalk(md.Model):
	"""
	Peng, C. K., Buldyrev, S. V., Goldberger, A. L., Havlin, S., Sciortino, F., Simons, M., & Stanley, H. E. (1992). Long-range correlations in nucleotide sequences. Nature, 356(6365), 168-170.
	"""
	signature = "DnaWalk"

	def __init__(self):
		self.base_maps = {'A':1, 'T':-1, 'C':-1, 'G':1}

	def get_value(self, base): return self.base_maps[base]
	
	def start_encoding(self, raw_sequence):
		self.len_raw_seq = len(raw_sequence)
		self.encoded_sequence = md.np.zeros((self.len_raw_seq))
		self.encoded_sequence[0] = self.get_value(raw_sequence[0])

	def map_dna_walk(self, base, pos):
		self.encoded_sequence[pos] = self.encoded_sequence[pos-1] + self.get_value(base)
		
	def encode_one(self, raw_sequence):
		self.start_encoding(raw_sequence)
		try: md.np.array(tuple(map(self.map_dna_walk, raw_sequence, range(1, self.len_raw_seq))))
		except Exception as e: raise md.ModelException(type(e).__name__)
		return self.encoded_sequence
		

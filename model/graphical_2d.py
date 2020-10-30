import seqreppy.model.model as md

class Liao(md.Model):
	"""	
	YAU, Stephen S.‐T. et al. DNA sequence representation without degeneracy. Nucleic acids research, v. 31, n. 12, p. 3078-3080, 2003.
	"""

	signature = "Liao"

	def __init__(self, m=3/4, n=0.5):
		self.n = n
		self.m = m
			
	def start_encoding(self, raw_sequence):
		self.count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
		self.len_encoded_seq = len(raw_sequence) + 1
		self.encoded_sequence = md.np.zeros((2, self.len_encoded_seq))

	def map_liao(self, base, pos):
		self.count[base] += 1
		self.encoded_sequence[0][pos] = self.m*(self.count['A'] + self.count['T']) + md.math.sqrt(self.n)*(self.count['G']+self.count['C'])			   
		self.encoded_sequence[1][pos] = md.math.sqrt(self.n)*(self.count['T']-self.count['A']) + self.m*(self.count['C']-self.count['G']) 
			
	def encode_one(self, raw_sequence):
		self.start_encoding(raw_sequence)
		try: tuple(map(self.map_liao, raw_sequence, range(1, self.len_encoded_seq)))
		except Exception as e: raise md.ModelExc(type(e).__name__)
		return self.encoded_sequence  

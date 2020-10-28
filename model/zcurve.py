import seqreppy.model.model as md

class Zcurve(md.Model):
	"""
	ZHANG, Ren; ZHANG, Chun-Ting. Z curves, an intutive tool for visualizing and analyzing the DNA sequences. Journal of Biomolecular Structure and Dynamics, v. 11, n. 4, p. 767-782, 1994.
	"""
	signature = "Zcurve"

	def start_encoding(self, raw_sequence):
		self.count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
		self.len_raw_seq = len(raw_sequence)
		self.encoded_sequence = md.np.zeros((3, self.len_raw_seq+1))

	def map_zcurve(self, base, pos):
		self.count[base] += 1
		self.encoded_sequence[0][pos] = (self.count.get('A') + self.count.get('G')) - (self.count.get('C') + self.count.get('T'))
		self.encoded_sequence[1][pos] = (self.count.get('A') + self.count.get('C')) - (self.count.get('G') + self.count.get('T'))
		self.encoded_sequence[2][pos] = (self.count.get('A') + self.count.get('T')) - (self.count.get('G') + self.count.get('C'))


	def encode_one(self, raw_sequence):
		self.start_encoding(raw_sequence)
		try: tuple(map(self.map_zcurve, raw_sequence, range(1, self.len_raw_seq+1)))
		except Exception as e: raise md.ModelExc(type(e).__name__)
		return self.encoded_sequence
	
	

	
		
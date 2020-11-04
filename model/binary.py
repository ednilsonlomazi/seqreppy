import seqreppy.model.model as md

class Binary2B(md.Model):
	""" Ranawana, R. and Palade, V. (2005) “A Neural network based multi-classifier system
		for gene identification in DNA sequence”, Neural Computing and Applications, v.
		14, n. 2, p. 122-131. """
	
	signature = "Binary2B"

	def __init__(self):
		self.binaries = {'A': (0,0), 'T': (0,1), 'C': (1,1), 'G': (1,0)}

	def get_bin_value(self, base): return self.binaries[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_bin_value, raw_sequence))).reshape((2*len(raw_sequence)))
		except Exception as e: raise md.ModelExc(type(e).__name__)


class Binary4B(md.Model):
	"""Demeler, B. and Zhou, G. W. (1991) “Neural network optimization for E.coli promoter
		prediction”, Nucleic Acids Res., v. 19, n.7, p. 1539-1599."""
	
	signature = "Binary4B"

	def __init__(self):
		self.binaries = {'A': (1,0,0,0), 'T': (0,1,0,0), 'G': (0,0,1,0), 'C': (0,0,0,1)}

	def get_bin_value(self, base): return self.binaries[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_bin_value, raw_sequence))).reshape((4*len(raw_sequence)))
		except Exception as e: raise md.ModelExc(type(e).__name__)

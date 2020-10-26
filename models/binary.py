import seqreppy.models.model as md

class Binary2B(md.Model):
	""" Ranawana, R. and Palade, V. (2005) “A Neural network based multi-classifier system
		for gene identification in DNA sequence”, Neural Computing and Applications, v.
		14, n. 2, p. 122-131. """
	
	signature = "Binary2B"

	def __init__(self):
		self.binaries = {'A': bin(0), 'T': bin(1), 'C': bin(3), 'G': bin(2)}

	def get_bin_value(self, base): return self.binaries[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_bin_value, raw_sequence)))
		except Exception as e: raise md.ModelException(type(e).__name__)


class Binary4B(md.Model):
	"""Demeler, B. and Zhou, G. W. (1991) “Neural network optimization for E.coli promoter
		prediction”, Nucleic Acids Res., v. 19, n.7, p. 1539-1599."""
	
	signature = "Binary4B"

	def __init__(self):
		self.binaries = {'A': bin(4), 'T': bin(8), 'C': bin(1), 'G': bin(2)}

	def get_bin_value(self, base): return self.binaries[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_bin_value, raw_sequence)))
		except Exception as e: raise md.ModelException(type(e).__name__)

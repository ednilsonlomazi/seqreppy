import seqreppy.models.model as md
 
class MolecularMass(md.Model):
	"""Stanley, H. E., Buldyrev, S. V., Goldberger, A. L., Goldberger, Z. D., Havlin, S., Mantegna, R. N., ... & Simons, M. (1994). Statistical mechanics in biology: how ubiquitous are long-range correlations?. Physica A: Statistical Mechanics and its Applications, 205(1-3), 214-253."""
	signature = "MolecularMass"

	def __init__(self):
		self.mms = {'A': 134, 'T': 125, 'C': 110, 'G': 150}

	def get_mass(self, base): return self.mms[base] 

	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_mass, raw_sequence)))
		except Exception as e: raise md.ModelException(type(e).__name__)
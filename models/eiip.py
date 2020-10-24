import seqreppy.models.model as md

class Eiip(md.Model):
	""" Nair, A. S., Sreenadhan, S. P. (2006) “A coding measure scheme employing electron-
		ion interaction pseudopotential (EIIP)”, Bioinformation, v. 1, n. 6, p. 197."""

	signature = "Eiip"

	def __init__(self):
		self.eiips = {'A': 0.1260, 'T': 0.1335, 'C': 0.1340, 'G': 0.0806}

	def get_eiip(self, base): return self.eiips.get(base) 
			
	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_eiip, raw_sequence)))
		except Exception: raise md.ModelException(0)
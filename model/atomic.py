import seqreppy.model.model as md

class Atomic(md.Model):
	""" Holden, T., Subramaniam, R., Sullivan, R., Cheung, E., Schneider, C., Tremberger Jr,
		G., Flamholz, A., Lieberman, D. H., Cheung, T. D. (2007) “ATCG nucleotide
		fluctuation of Deinococcus radiodurans radiation genes”, In: Instruments, Methods,
		and Missions for Astrobiology X, International Society for Optics and Photonics, v.
		6694, p. 669417."""
	signature = "Atomic"

	def __init__(self):
		self.atomic_numbers = {'A': 70, 'T': 66, 'C': 58, 'G': 78}

	def get_atomic_number(self, base): return self.atomic_numbers[base] 
			
	def encode_one(self, raw_sequence):
		try: return md.np.array(tuple(map(self.get_atomic_number, raw_sequence)))
		except Exception as e: raise md.ModelExc(type(e).__name__)

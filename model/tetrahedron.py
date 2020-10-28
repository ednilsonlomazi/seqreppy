import seqreppy.model.model as md
	
class Tetrahedron(md.Model):
	"""
	B.D. Silverman and R. Linsker, “A measure of DNA periodicity,”J.Theor. Biol., vol. 118, pp. 295-300, 1986.
	"""
	signature = "Tetrahedron"

	def __init__(self):
		self.bin_indicators = {'A': (1,0,0,0), 'T': (0,1,0,0), 'C': (0,0,1,0), 'G': (0,0,0,1)}

	def get_bin_indicator(self, base): return self.bin_indicators[base]
		 
	def encode_one(self, raw_sequence):
		try:
			seq_bin_indicators = md.np.transpose(md.np.array(tuple(map(self.get_bin_indicator, raw_sequence))))	
			return md.np.array(((md.math.sqrt(2)/3)*(2*seq_bin_indicators[1]-seq_bin_indicators[2]-seq_bin_indicators[3]),
						 	 (md.math.sqrt(6)/3)*(seq_bin_indicators[2]-seq_bin_indicators[3]),
						 	 (1/3)*(3*seq_bin_indicators[0]-seq_bin_indicators[2]-seq_bin_indicators[3]-seq_bin_indicators[1])))
		except Exception as e: raise md.ModelExc(type(e).__name__)


		
			

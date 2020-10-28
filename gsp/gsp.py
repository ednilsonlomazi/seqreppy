import numpy as np
from seqreppy.gsp.gsp_exception import GspExc


class Gsp():
	"""docstring for Gsp"""
	
	def make_power_spectrum(self, encoded_sequence):
		try: return np.abs(np.fft.fftn(encoded_sequence))**2
		except Exception: raise GspExc(0)

	def get_spectral_content(self, encoded_sequence): 
		return np.sum(self.make_power_spectrum(encoded_sequence), axis=0)
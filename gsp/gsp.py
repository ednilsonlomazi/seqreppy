import numpy as np
from seqreppy.gsp.gsp_exception import GspExc


class Gsp():
	"""docstring for Gsp"""
	
	def map_axis(self, axis): return np.abs(np.fft.fft(axis))**2 

	def make_power_spectrum(self, encoded_sequence):
		if encoded_sequence.ndim == 1: return np.abs(np.fft.fft(encoded_sequence))**2 
		try: return np.array(tuple(map(self.map_axis, encoded_sequence)))
		except Exception: raise GspExc(0)

	def get_spectral_content(self, encoded_sequence): 
		return np.sum(self.make_power_spectrum(encoded_sequence), axis=0)
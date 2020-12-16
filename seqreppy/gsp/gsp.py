import numpy as np

def map_axis(axis): return np.abs(np.fft.fft(axis))**2 

def power_spectrum(encoded_sequence):
	encoded_sequence = np.array(encoded_sequence)
	if encoded_sequence.ndim == 1: return np.abs(np.fft.fft(encoded_sequence))**2 
	return np.array(tuple(map(map_axis, encoded_sequence)))

def spectral_content(encoded_sequence): 
	return np.sum(power_spectrum(encoded_sequence), axis=0)

def apply_gsp(gsp_function, results):
	values = tuple(results.values())
	gsps = np.array( tuple(tuple(map(gsp_function, values[i])) for i in range(len(values)))  )
	return dict(zip(results.keys(), gsps ))
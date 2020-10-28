import numpy as np
import math
from seqreppy.model.model_exception import ModelExc

class Model(object):
	"""docstring for Model"""
	
	signature = '' 

	def encode_one(self, raw_sequence): pass

	def encode_many(self, raw_sequences): return tuple(map(self.encode_one, raw_sequences))
		
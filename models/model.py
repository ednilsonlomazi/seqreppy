import numpy as np
import math
from seqreppy.models.model_exception import ModelException

class Model(object):
	"""docstring for Model"""
	
	signature = '' 

	def encode_one(self, raw_sequence): pass

	def encode_many(self, raw_sequences): return tuple(map(self.encode_one, raw_sequences))
		
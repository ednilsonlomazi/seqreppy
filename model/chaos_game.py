import seqreppy.model.model as md

class CGR(md.Model):
	""" Jeffrey, H. J. (1990) “Chaos game representation of gene structure”, Nucleic acids
		research, v. 18, n. 8, p. 2163-2170."""

	signature = "CGR"

	def __init__(self):
		self.corners = {'A':(0,0), 'T':(1,0),'U':(1,0), 'C':(0,1), 'G':(1,1)}
 
	def start_encoding(self, raw_sequence):
		self.len_seq = len(raw_sequence)
		self.encoded_sequence = md.np.zeros((2, self.len_seq))
		self.encoded_sequence[0][0] = 0.5
		self.encoded_sequence[1][0] = 0.5 

	def map_cgr(self, char, pos):
		coordenate = self.corners[char]
		self.encoded_sequence[0][pos] = 0.5*(self.encoded_sequence[0][pos-1]+coordenate[0])
		self.encoded_sequence[1][pos] = 0.5*(self.encoded_sequence[1][pos-1]+coordenate[1])
		
	def encode_one(self, raw_sequence):
	    self.start_encoding(raw_sequence)
	    try: tuple(map(self.map_cgr, raw_sequence, range(1, self.len_seq)))
	    except Exception as e: raise md.ModelExc(type(e).__name__)
	    return self.encoded_sequence
	 

class IntegerCGR(md.Model):
	""" Yin, C. (2019) “Encoding and Decoding DNA Sequences by Integer Chaos Game
		Representation”, Journal of Computational Biology, v. 26, n. 2, p. 143-151."""

	signature = "IntegerCGR"

	def __init__(self):
		self.corners = {'A':(1,1), 'T':(-1,1), 'U':(-1,1), 'C':(-1,-1), 'G':(1,-1)}

	def start_encoding(self, raw_sequence):
		self.len_seq = len(raw_sequence)
		assert self.len_seq <= 1024 # futuramente, criarei uma exceção bonitinha para isso
		self.encoded_sequence = md.np.zeros((2, self.len_seq))
		try:
			coordenate = self.corners.get(raw_sequence[0])
			self.encoded_sequence[0][0] = coordenate[0]
			self.encoded_sequence[1][0] = coordenate[1]
		except Exception as e: raise md.ModelExc(type(e).__name__)

	def map_icgr(self, char, pos):
		coordenate = self.corners[char]
		self.encoded_sequence[0][pos] = self.encoded_sequence[0][pos-1] + (2**(pos))*coordenate[0]
		self.encoded_sequence[1][pos] = self.encoded_sequence[1][pos-1] + (2**(pos))*coordenate[1]

	def encode_one(self, raw_sequence):
	    self.start_encoding(raw_sequence)
	    try: tuple(map(self.map_icgr, raw_sequence, range(1, self.len_seq)))
	    except Exception as e: raise md.ModelExc(type(e).__name__)
	    return self.encoded_sequence 

		

""" OBSERVATION: IntegerCGR original algorithM returns (X, Y, N), where N is the sequence lenght. But, N is used only for decoding, and here we are foucus only in encoding. Then, i just return (X,Y)"""
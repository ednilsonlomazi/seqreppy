import numpy as np
from seqreppy.data.data_exception import DataExc

class Data(object): 		 

	def __init__(self):
		self.start()
		
	def start(self):
		self.sequences_data = []
		self.sequences_info = []
		self.sequences_data_temp = []

	def map_value_format(self, value): return "{}".format(value)

	def map_encoded_sequence(self, axis): return ','.join(tuple(map(self.map_value_format, axis)))

	def get_encoded_sequence_str(self, encoded_sequence): 
		if encoded_sequence.ndim == 1:  return ','.join(tuple(map(self.map_value_format, encoded_sequence)))
		return '\n'.join(tuple(map(self.map_encoded_sequence, encoded_sequence)))	

	def map_lines(self, sequence_info, encoded_sequence):
		return ''.join(('>', sequence_info, '\n', self.get_encoded_sequence_str(encoded_sequence), '\n\n')) 
	
	def map_dirs(self, directory, result):
		with open(directory, 'w') as file:
			file.write(''.join(tuple(map(self.map_lines, self.sequences_info, result))))

	def save_results(self, directories, results_dict): tuple(map(self.map_dirs, directories, tuple(results_dict.values())))			
	
	def map_axis(self, number): return eval(number)

	def map_info_data_split(self, line):
		if line[0] == '>': self.sequences_info.append(line[:-1])
		elif line[0] != '\n': self.sequences_data_temp.append(tuple(map(self.map_axis, line[:-1].split(','))))
		else:
			if len(self.sequences_data_temp) == 1: 
				self.sequences_data.append(np.array(self.sequences_data_temp[0]))
			else: self.sequences_data.append(np.array(self.sequences_data_temp))
			self.sequences_data_temp = []

	def get_result(self, directory):
		self.start()
		with open(directory) as file:
			try: tuple(map(self.map_info_data_split, file.readlines()))
			except Exception as e: raise DataExc(type(e).__name__)  
		self.sequences_data = tuple(self.sequences_data)
		return self.sequences_data
		
	def map_fasta_file(self, part):
		temp = part.split('\n')
		self.sequences_info.append(temp[0])
		self.sequences_data.append(''.join(temp[1:]))  

	def read_fasta(self, directory):
		self.start()
		with open(directory) as file:
			file_splited = file.read().split('>')[1:] 
			try:
				file_splited[0]
				tuple(map(self.map_fasta_file, file_splited))
			except Exception as e: raise DataExc(type(e).__name__)
	
		return self.sequences_data, self.sequences_info
	 
	 
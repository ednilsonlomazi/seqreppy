from seqreppy.config import default_results_txt, model_signatures
from seqreppy.data.data import Data
from seqreppy.view.view import View
from seqreppy.model.chaos_game import CGR, IntegerCGR
from seqreppy.model.complex import Complex
from seqreppy.model.dna_walk import DnaWalk
from seqreppy.model.graphical_2d import Liao
from seqreppy.model.tetrahedron import Tetrahedron 
from seqreppy.model.zcurve import Zcurve
from seqreppy.model.voss import Voss
from seqreppy.model.atomic import Atomic
from seqreppy.model.molecular_mass import MolecularMass
from seqreppy.model.eiip import Eiip
from seqreppy.model.binary import Binary2B, Binary4B
from seqreppy.model.paired_numeric_mapping import PairedNumericMapping
from seqreppy.model.real import Real 
from seqreppy.model.integer import Integer
from seqreppy.encoder.encoder_exception import EncoderExc
from seqreppy.gsp.gsp import Gsp
  
class SeqRep(object): 

	def __init__(self):
		self.data = Data()
		
	def set_fasta_file(self, fasta_directory):
		self.data.read_fasta(fasta_directory)

	def set_raw_sequences(self, raw_sequences, sequences_info=None):
		if sequences_info: self.data.sequences_info = sequences_info
		self.data.sequences_data = raw_sequences
 
	def model_mapping(self, signature):
		if signature not in model_signatures: raise EncoderExc(0, signature)
		return eval(''.join([signature, "()"]))

	def set_models(self, *signatures): self.models = tuple(map(self.model_mapping, signatures))

	def perform_power_spectrum(self, dnas_encoded):
		try:
			if dnas_encoded[0].ndim == 1: return tuple(map(self.signal_processing.make_power_spectrum, dnas_encoded))
			else: return tuple(map(self.signal_processing.get_spectral_content, dnas_encoded))	
		except AttributeError:
			self.signal_processing = Gsp()
			return self.perform_power_spectrum(dnas_encoded)
		
	def map_encoding(self, model): return model.encode_many(self.data.sequences_data)
	
	def map_signatures(self, model): return model.signature

	def perform_encoding(self, gsp=False):
		self.gsp = gsp
		self.results = dict(zip(map(self.map_signatures, self.models), map(self.map_encoding, self.models)))
		if gsp: self.results = dict(zip(map(self.map_signatures, self.models), map(self.perform_power_spectrum, self.results.values()))) 	
		return self.results

	def get_sequences_info(self): return self.data.sequences_info

	def map_default_dirs(self, model): return ''.join((default_results_txt, model.signature)) 

	def save_results(self, *directories, **kargs):
		if not directories: directories = tuple(map(self.map_default_dirs, self.models))
		else:
			if len(directories) != len(self.models): raise EncoderExc(3)
		self.data.save_results(directories, self.results, **kargs)
	
	def get_results(self, model_dir_dict, gsp=False):
		self.gsp = gsp
		directories = model_dir_dict.values()
		self.results = dict(zip(tuple(model_dir_dict.keys()), map(self.data.get_result, directories)))
		return self.results
	
	def verify_figure(self, model_signature, kargs):
		try: self.visual_maker
		except AttributeError: self.visual_maker = View()
		if not kargs.get("show") and not kargs.get("save"): kargs["show"] = True    

	def verify_seq_encoded(self, model_signature, seq_id):
		try: return self.results[model_signature][seq_id]
		except KeyError as e: raise EncoderExc(0, model_signature, type(e).__name__)
		except IndexError as e: raise EncoderExc(0, seq_id, type(e).__name__)
		
	def generate_figure(self, seq_id, model_signature, **kargs):
		seq_encoded = self.verify_seq_encoded(model_signature, seq_id)
		self.verify_figure(model_signature, kargs)
		if self.gsp: 
			if kargs.get("show"): self.visual_maker.visualize_power_spectrum(model_signature, seq_encoded)
			if kargs.get("save"): self.visual_maker.save_power_spectrum(model_signature, seq_encoded, **kargs)
		else:
			if (model_signature == "Voss" or (seq_encoded.ndim == 1 and model_signature != "DnaWalk")):
				raise EncoderExc(1, model_signature)
			if kargs.get("show"): self.visual_maker.visualize(model_signature, seq_encoded)
			if kargs.get("save"): self.visual_maker.save_figure(model_signature, seq_encoded, **kargs) 	
 

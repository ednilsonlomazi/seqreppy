import seqrepc as core

seqs_info = ()
seqs_data = ()
full_result = ()
source_directory = ""

def collect_fasta(source):
	global seqs_data, seqs_info
	seqs_data, seqs_info = core.collect_fasta(source);

def map_info_to_bytes(i): return bytes(seqs_info[i], "utf-8") 
 
def save_results(results, *dsts):
	mp_signatures = tuple(results.keys())
	num_seqs = len(results[mp_signatures[0]])
	assert len(mp_signatures) == len(dsts)
	for mp_signature, dst in zip(mp_signatures, dsts):
		core.store(results[mp_signature], tuple(map(map_info_to_bytes, range(num_seqs))), mp_signature, dst)

def map_full_result(mp_signature, source):
	return core.collect_encodings(mp_signature, source)

def map_simplify_result(i): return full_result[i][0]

def get_results(dict_results):
	global full_result
	mp_signatures = dict_results.keys()
	full_result = tuple(map(map_full_result, mp_signatures, dict_results.values()))
	simplified_results = tuple(map(map_simplify_result, range(len(full_result))))
	return dict(zip(mp_signatures, simplified_results))

def encode_from_file(mp_signatures, source):
	if(source_directory != source): collect_fasta(source)
	if((type(mp_signatures) != str)):
		results = tuple(tuple(core.encode(mp_signature, ''.join(seq)) for seq in seqs_data) for mp_signature in mp_signatures)
		return dict(zip(mp_signatures, results))
	else:
		results = tuple(core.encode(mp_signatures, ''.join(seq)) for seq in seqs_data)
		return {mp_signatures: results}

def encode_from_strings(mp_signatures, strings):
	if(len(strings) > 0):
		if((type(mp_signatures) != str)):
			results = tuple(tuple(core.encode(mp_signature, seq) for seq in strings) for mp_signature in mp_signatures)
			return dict(zip(mp_signatures, results))
		else:
			results = tuple(core.encode(mp_signatures, seq) for seq in strings)
			return {mp_signatures: results}



	
# i supose that the user will not save, again, the results that is already on disk. If he do this thing, we got an arror on get results. 
# get_results is similar to encode_from_*. She think only on seqs_encoded, not in seqs_info. If the user wants seqs_info,
# he can see full_result
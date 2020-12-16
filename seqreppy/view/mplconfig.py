import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

mplconfig = {
	"atomic": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"cgr": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 1}, 'marker':'.'},
	"icgr": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"imaginary": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.5}, 'marker':'-'},
	"dna_walk": {'pltconfig': {"xlabel": "Distância Nucleotídica 'L'", "ylabel": 'Dna Walk (L)'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"liao": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"eiip": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"binary2b": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"binary4b": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"integer": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"molecular_mass": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"PairedNumericMapping": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"real": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"tetrahedron": {'pltconfig': {"xlabel": "x", "ylabel": 'y', "zlabel": 'z'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"voss": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"zcurve": {'pltconfig': {"xlabel": "x", "ylabel": 'y', "zlabel": 'z'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'}	
}
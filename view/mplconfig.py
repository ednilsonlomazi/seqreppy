import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

mplconfig = {
	"Atomic": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"CGR": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 1}, 'marker':'.'},
	"IntegerCGR": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"Complex": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.5}, 'marker':'-'},
	"DnaWalk": {'pltconfig': {"xlabel": "Distância Nucleotídica 'L'", "ylabel": 'Dna Walk (L)'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"Liao": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Eiip": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"Binary2B": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Binary4B": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Integer": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"MolecularMass": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.1}, 'marker':'-'},
	"PairedNumericMapping": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Real": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Tetrahedron": {'pltconfig': {"xlabel": "x", "ylabel": 'y', "zlabel": 'z'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Voss": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'},
	"Zcurve": {'pltconfig': {"xlabel": "x", "ylabel": 'y', "zlabel": 'z'}, 'plotconfig':{'c': "black", "markersize": 0.3}, 'marker':'-'}	
}


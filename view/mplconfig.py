import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

mplconfig = {
	"Atomic": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"CGR": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 1}},
	"IntegerCGR": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Complex": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.5}},
	"DnaWalk": {'pltconfig': {"xlabel": "Distância Nucleotídica 'L'", "ylabel": 'Dna Walk (L)'}, 'plotconfig':{'c': "black", "markersize": 0.5}, "marker":'-'},
	"Yau": {'pltconfig': {"xlabel": "x", "ylabel": 'y'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Eiip": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Binary2B": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Binary4B": {'pltconfig': {"xlabel": "Frequência", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Integer": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"MolecularMass": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"PairedNumericMapping": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Real": {'pltconfig': {"xlabel": "Frequency", "ylabel": 'Power Spectrum'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Tetrahedron": {'pltconfig': {"xlabel": "x", "ylabel": 'y', "zlabel": 'z'}, 'plotconfig':{'c': "black", "markersize": 0.3}},
	"Voss": {"xlabel": 'Frequency', "ylabel": 'Power Spectrum', 'c': "black", "markersize": 0.3},
	"Zcurve": {'pltconfig': {"xlabel": "x", "ylabel": 'y', "zlabel": 'z'}, 'plotconfig':{'c': "black", "markersize": 0.3}}	
}


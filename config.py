import pathlib

default_results_txt = str(pathlib.Path(__file__).parent) + "/results/txt/"
default_results_img = str(pathlib.Path(__file__).parent) + "/results/img/" 

model_signatures = ("Atomic", "CGR", "Complex", "DnaWalk", 
					"Yau", "Eiip", "Binary2B", "Binary4B", "Integer", "IntegerCGR", "MolecularMass",
					"PairedNumericMapping", "Real", "Tetrahedron", "Voss", "Zcurve")
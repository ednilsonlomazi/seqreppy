import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
import datetime
from seqreppy.config import default_results_img
from seqreppy.view.mplconfig import mplconfig 


def make_1D(seq_encoded, model_signature):
	config = mplconfig.get(model_signature)
	pltconfig = config.get("pltconfig")
	plt.clf()
	plt.plot(seq_encoded, config.get("marker"), **config.get("plotconfig"))
	plt.xlabel(pltconfig.get("xlabel"))
	plt.ylabel(pltconfig.get("ylabel"))
	plt.ticklabel_format(style='sci', scilimits=(10,1))
	plt.tight_layout() 
	return plt
	
def make_2D(seq_encoded, model_signature):
	config = mplconfig.get(model_signature)
	pltconfig = config.get("pltconfig")
	plt.clf()
	plt.plot(seq_encoded[0], seq_encoded[1], config.get("marker"), **config.get("plotconfig"))
	plt.xlabel(pltconfig.get("xlabel"))
	plt.ylabel(pltconfig.get("ylabel"))
	plt.ticklabel_format(style='sci', scilimits=(10,1))
	plt.tight_layout()
	return plt
	
def make_3D(seq_encoded, model_signature):
	config = mplconfig.get(model_signature)
	pltconfig = config.get("pltconfig")
	ax3d = Axes3D(plt.figure())	
	ax3d.plot(xs=seq_encoded[0], ys=seq_encoded[1], zs=seq_encoded[2], zdir='z', **config.get("plotconfig"))
	ax3d.set_xlabel(pltconfig.get("xlabel"))
	ax3d.set_ylabel(pltconfig.get("ylabel"))
	ax3d.set_zlabel(pltconfig.get("zlabel"))
	ax3d.ticklabel_format(style='sci', scilimits=(10,1))
	return plt

def build_power_spectrum(model_signature, power_spectrum, kargs):
	start = kargs.get("start")
	if(not start): start = 1
	end = kargs.get("end")
	config = mplconfig.get(model_signature)
	pltconfig = config.get("pltconfig")
	plt.clf()
	plt.plot(power_spectrum[start:end], config.get("marker"), **config.get("plotconfig"))
	plt.xlabel(pltconfig.get("xlabel"))
	plt.ylabel(pltconfig.get("ylabel"))
	plt.ticklabel_format(style='sci', scilimits=(10,1))
	plt.tight_layout()
	return plt


def fname_verify(img_kargs):
	if "fname" not in img_kargs:
		img_kargs["fname"] = ''.join(( 
									 "r_{}_".format(datetime.datetime.now().day),
									 "{}_".format(datetime.datetime.now().hour),
									 "{}_".format(datetime.datetime.now().minute),
									 "{}.png".format(datetime.datetime.now().microsecond)
								))


def visualize_power_spectrum(model_signature, power_spectrum, **kargs):
	build_power_spectrum(model_signature, power_spectrum, kargs).show()

def save_power_spectrum(model_signature, power_spectrum, **img_kargs):
	fname_verify(img_kargs)
	build_power_spectrum(model_signature, power_spectrum).savefig(**img_kargs)

def visualize(model_signature, seq_encoded):
	if(type(seq_encoded) != np.ndarray): seq_encoded = np.array(seq_encoded)
	num_axis_zero = np.ma.size(seq_encoded, axis=0)
	if seq_encoded.ndim == 1:
		make_1D(seq_encoded, model_signature).show()
	elif num_axis_zero == 2:
		make_2D(seq_encoded, model_signature).show()
	elif num_axis_zero == 3:
		make_3D(seq_encoded, model_signature).show()

def save_figure(model_signature, seq_encoded, **img_kargs):
	if(type(seq_encoded) != np.ndarray): seq_encoded = np.array(seq_encoded)
	fname_verify(img_kargs)
	num_axis_zero = np.ma.size(seq_encoded, axis=0)
	try:
		if seq_encoded.ndim == 1:
			make_1D(seq_encoded, model_signature).savefig(**img_kargs)
		elif num_axis_zero == 2:
			make_2D(seq_encoded, model_signature).savefig(**img_kargs)
		elif num_axis_zero == 3:
			make_3D(seq_encoded, model_signature).savefig(**img_kargs)
	except Exception as e: raise ViewExc(type(e).__name__)


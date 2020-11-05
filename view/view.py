import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
import datetime
from seqreppy.config import default_results_img
from seqreppy.view.mplconfig import mplconfig 
from seqreppy.view.view_exception import ViewExc

class View(object):
	"""docstring for View""" 


	def make_1D(self, seq_encoded, model_signature):
		config = mplconfig.get(model_signature)
		pltconfig = config.get("pltconfig")
		plt.clf()
		plt.plot(seq_encoded, config.get("marker"), **config.get("plotconfig"))
		plt.xlabel(pltconfig.get("xlabel"))
		plt.ylabel(pltconfig.get("ylabel"))
		plt.ticklabel_format(style='sci', scilimits=(10,1))
		plt.tight_layout() 
		return plt
		
	def make_2D(self, seq_encoded, model_signature):
		config = mplconfig.get(model_signature)
		pltconfig = config.get("pltconfig")
		plt.clf()
		plt.plot(seq_encoded[0], seq_encoded[1], config.get("marker"), **config.get("plotconfig"))
		plt.xlabel(pltconfig.get("xlabel"))
		plt.ylabel(pltconfig.get("ylabel"))
		plt.ticklabel_format(style='sci', scilimits=(10,1))
		plt.tight_layout()
		return plt
		
	def make_3D(self, seq_encoded, model_signature):
		config = mplconfig.get(model_signature)
		pltconfig = config.get("pltconfig")
		ax3d = Axes3D(plt.figure())	
		ax3d.plot(xs=seq_encoded[0], ys=seq_encoded[1], zs=seq_encoded[2], zdir='z', **config.get("plotconfig"))
		ax3d.set_xlabel(pltconfig.get("xlabel"))
		ax3d.set_ylabel(pltconfig.get("ylabel"))
		ax3d.set_zlabel(pltconfig.get("zlabel"))
		ax3d.ticklabel_format(style='sci', scilimits=(10,1))
		return plt

	def make_subplots(self, type_plots, title_plots, results, seq_id): # emergencial code for article publication
		fig, axs = plt.subplots(*type_plots, sharex=False, sharey=False)
		for seq, signature, ax, titile in results.values(), results.keys(), axs, title_plots:
			num_axis_zero = np.ma.size(seq[seq_id], axis=0)	
			try:
				if signature == "DnaWalk": ax = self.make_1D(seq, signature)
				elif seq.ndim == 1: build_power_spectrum(seq, signature) 
				elif num_axis_zero == 2: ax = self.make_2D(*seq, signature)
				ax.set_title(titile)
			except Exception as e: raise ViewExc(type(e).__name__)
		return plt

	def build_power_spectrum(self, model_signature, power_spectrum):
		config = mplconfig.get(model_signature)
		pltconfig = config.get("pltconfig")
		plt.clf()
		plt.plot(power_spectrum[1:], config.get("marker"), **config.get("plotconfig"))
		plt.xlabel(pltconfig.get("xlabel"))
		plt.ylabel(pltconfig.get("ylabel"))
		plt.ticklabel_format(style='sci', scilimits=(10,1))
		plt.tight_layout()
		return plt

	
	def fname_verify(self, img_kargs):
		if "fname" not in img_kargs:
			img_kargs["fname"] = ''.join((default_results_img, 
											 "r_{}_".format(datetime.datetime.now().day),
											 "{}_".format(datetime.datetime.now().hour),
											 "{}_".format(datetime.datetime.now().minute),
											 "{}.png".format(datetime.datetime.now().microsecond)))

	def visualize_power_spectrum(self, model_signature, power_spectrum):
		self.build_power_spectrum(model_signature, power_spectrum).show()

	def save_power_spectrum(self, model_signature, power_spectrum, **img_kargs):
		self.fname_verify(img_kargs)
		self.build_power_spectrum(model_signature, power_spectrum).savefig(**img_kargs)

	def visualize(self, model_signature, seq_encoded):
		num_axis_zero = np.ma.size(seq_encoded, axis=0)
		try:
			if seq_encoded.ndim == 1:
				self.make_1D(seq_encoded, model_signature).show()
			elif num_axis_zero == 2:
				self.make_2D(seq_encoded, model_signature).show()
			elif num_axis_zero == 3:
				self.make_3D(seq_encoded, model_signature).show()
		except Exception as e: raise ViewExc(type(e).__name__)

	def save_figure(self, model_signature, seq_encoded, **img_kargs):
		self.fname_verify(img_kargs)
		num_axis_zero = np.ma.size(seq_encoded, axis=0)
		try:
			if seq_encoded.ndim == 1:
				self.make_1D(seq_encoded, model_signature).savefig(**img_kargs)
			elif num_axis_zero == 2:
				self.make_2D(seq_encoded, model_signature).savefig(**img_kargs)
			elif num_axis_zero == 3:
				self.make_3D(seq_encoded, model_signature).savefig(**img_kargs)
		except Exception as e: raise ViewExc(type(e).__name__)
	
"""	def visualize_subplots(self, *args): self.make_subplots(*args).show()

	def save_subplots(self, *args, **img_kargs): self.make_subplots(*args).savefig(**img_kargs)"""
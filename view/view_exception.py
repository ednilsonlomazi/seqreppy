class ViewException(Exception):
	"""docstring for ViewException"""
	def __init__(self, arg):
		super(ViewException, self).__init__()
		self.arg = arg
		
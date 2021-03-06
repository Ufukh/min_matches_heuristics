# An object of the class corresponds a solution of either the transhipment or the transportation MIP,
# i.e. specifies the required heat exchangers and the way heat is transferred.
class Heat_Exchange:

	def __init__(self,*args):
		
		self.model=args[0]
		self.n = args[1] # number of heaters
		self.m = args[2] # number of coolers
		self.k = args[3] # number of temperature intervals
		
		if self.model=='transshipment':
			self.matches=args[4]
			self.y = args[5] # indicator vector of matches
			self.q = args[6]
			self.r = args[7]
		
		else:
			self.matches=args[4]
			self.y = args[5] # indicator vector of matches
			self.q = args[6] # vector

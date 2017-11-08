class Difference:
	def __init__(self, a):
	       self.__elements = a
	# Add your code here
       
    def computeDifference(self):
        maxNumber = max(self.__elements)
        minNumber = min(self.__elements)
        self.maximumDifference = maxNumber - minNumber
class console:
	def log(*other) -> None:
	    print(' '.join([str(i) for i in other]))
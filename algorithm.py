#library for smart grid algorithms

def overvoltage(v):
	if v>235:
		return 1
	elif v<225:
		return 2
	else:
		return 0

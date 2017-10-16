def simple_areas(*args):
	#print(type(args))
	import math
	if len(args)==3:
		P=float((args[2]+args[1]+args[0])/2)
		Square=round(float(math.sqrt(P*(P-args[0])*(P-args[1])*(P-args[2]))),2)
	elif len(args)==2:
		Square=round(float(args[1]*args[0]),2)
	else:
		Square=round(float(math.pi*args[0]/4*args[0]),2)
	print(len(args),Square)
	return Square

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
simple_areas(3)


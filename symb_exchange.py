def symb_exchange(line):
	exchanged=list(line)
	exchanged[len(line)-1]=line[0]
	exchanged[0]=line[len(line)-1]
	exchanged=''.join(exchanged)
	return exchanged

symb_exchange("length")

def sure_not(line):

#	print(line)
	if (line[0:4])=='not ':
		return line
	else:
		line='not '+line
	return line
sure_not('not sure')

def count_ingots(report):
    import string

    m = []
    for x in string.ascii_uppercase:
        for y in range(1,10):
            m.append("%s%d" % (x, y))

    c = 0
    for i in report.split(","):
        c += (m.index(i)+1)

    return c


count_ingots(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i', 'A', 'X', 'j', 'L', 'y', 's', 'K', 'g', 'p', 'r', 7, 'b'])

from datetime import *

def count_reports(full_report, from_date, to_date):
	listing = full_report.split()
	#print(type(out),out)
	#print(type(listing),listing,'\n',listing[::2],'\n',listing[1::2])
	entries = dict([(x, y) for x, y in zip(listing[::2], listing[1::2])])  #!!!!!!!До конца разобраться надо
	#print(entries)
	quantity=0
	init_date=datetime.strptime(from_date, "%Y-%m-%d")
	final_date=datetime.strptime(to_date, "%Y-%m-%d")
	for x in entries:
		current_date=datetime.strptime(x, "%Y-%m-%d")
		if (init_date<=current_date and current_date<=final_date):
			#print(entries[x].split(','))
			for y in entries[x].split(','):
				#print((int(ord(y[:1]))-65)*9 + int(y[1:2]))
				quantity+=(int(ord(y[:1]))-65)*9 + int(y[1:2])

	return quantity


count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31")

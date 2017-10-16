# 1.length 10 characters
# 2. one digit at least
# 3. one lowercase and one uppercase at least
# password - string
def golf(password):
    return True or False
password='bAse730onE'
from re import *
#patt=compile(r"^[0-9]{1,}[a-z]{1,}[A-Z]{1,}")
patt=compile(r"^(?=.*[A-Z]{1,})(?=.*[0-9]{1,})(?=.*[a-z]{1,}).{10,}$")
if patt.match(password):
	return True
else:
	return False

# Shortest solution golf=lambda d:9<len(d)and all(any(map(t,d))for t in(str.isdigit,str.isupper,str.islower))

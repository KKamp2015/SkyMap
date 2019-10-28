def ConvRA(RA):
	RA=RA.split(' ')
	RA1=float(RA[0])
	RA2=float(RA[1])
	RA3=float(RA[2])
	RA2=RA3+(RA3/60)
	RA1=RA1+(RA2/60)
	RA1*=15
	return RA1

def ConvDec(Dec1):
	Dec=Dec.split(' ')
	Dec1=float(Dec[0])
	Dec2=float(Dec[1])
	Dec3=float(Dec[2])
	if Dec1<0:
		Dec2=Dec2+(Dec3/60)
		Dec1=Dec1-(Dec2/60)
	else:
		Dec2=Dec2+(Dec3/60)
		Dec1=Dec1+(Dec2/60)
	return Dec1
'''
Keefe Kamp
This code was made for SPS4010 Stellar Structues and Interiors.
This code produces a sky map of Be stars using an aitoff projection with included boxes for telescope range for SARA Telescopes
'''
# Improting the needed packages
import matplotlib.pyplot as plt # allows plot to be made
import numpy as np # allows for conversion between radians and degress and second method to read text in.
from astroquery.simbad import Simbad
def ConvRA(RA):
	RA=RA.split(' ')
	out=RA[-1]
	for i in np.arange(-2,-(len(RA)+1),-1):
		out/=60
		out+=RA[i]
	out*=15
	return out

def ConvDec(Dec1):
	Dec=Dec.split(' ')
	s=np.sign(Dec[1])
	Dec[1]=np.abs(Dec[1])
	out=Dec[-1]
	for i in np.arange(-2,-(len(Dec)+1),-1):
		out/=60
		out+=Dec[i]
	out*=s
	return out
	

stars=stars=Simbad.query_criteria("sptypes='K'")
stars.more()
#Sets Global parameters 
plt.rc('axes', axisbelow=True)
#sets up plot
fig=plt.figure()#Creates plot
ax=fig.add_subplot(111,projection='aitoff')#puts plot into an Aitoff Projection
ax.grid(1)#turns grid lines on
#isolating Right Acsention(RA) array for manipulation
RA=[]
Dec=[]
K=0
for i in range(len(stars)):
	try:
		ratemp=ConvRA(stars['RA'][i])
		Dectemp=ConvRA(stars['DEC'][i])
		Dec.append(Dectemp)
		RA.append(ratemp)
	except:
		K+=1
print(K," not plotted")
x=np.array(RA)
#manipulating RA to be plot from -180 to 180
i=x>180# finding indecies above 180
x[i]-=360 #stubtracting 360 from RA<180 deg
x=-x

#making range boxs

ax.scatter(np.radians(x),np.radians(DEC),marker='*',s=1,color='k',label=None)

#relabeling tickmarks to hours
ax.set_xticklabels(np.array(['10h', '8h','6h','4h', '2h','0h','22h','20h','18h','16h','14h']),color='k')

label="WNMap.jpg"
plt.savefig(label,format='jpg',dpi=300)



'''
Keefe Kamp
This code was made for SPS4010 Stellar Structues and Interiors.
This code produces a sky map of Be stars using an aitoff projection with included boxes for telescope range for SARA Telescopes
'''
# Improting the needed packages
import matplotlib.pyplot as plt # allows plot to be made
import numpy as np # allows for conversion between radians and degress and second method to read text in.
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u
def ConvRA(RA):
	RA=RA.strip()
	RA=RA.split(' ')
	out=float(RA[-1])
	for i in np.arange(-2,-(len(RA)+1),-1):
		out/=60
		out+=float(RA[i])
	out*=15
	out=float(out)
	return out

def ConvDec(Dec):
	Dec=Dec.split(' ')
	s=np.sign(int(Dec[1]))
	Dec[1]=np.abs(int(Dec[1]))
	out=float(Dec[-1])
	for i in np.arange(-2,-(len(Dec)+1),-1):
		print (np.arange(-2,-(len(Dec)+1),-1))
		out/=60
		out+=float(Dec[i])
	out*=s
	out=float(out)
	return out
	

stars=stars=Simbad.query_criteria("sptypes='K'")
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
		Dectemp=ConvDec(stars['DEC'][i])
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

ax.scatter(np.radians(x),np.radians(Dec),marker='*',s=1,color='k',label=None,zorder=100)

#plotting Glactic Plane
#creating galactic plane in glatic coordinates
lon=np.arange(0,360)
ga=SkyCoord(b=0,l=lon,unit='deg',frame='galactic')
#transforrming into RA and DEC
ga=ga.transform_to('icrs')
#converinting to arrays and prettping RA to be plotted (-180,180) instead of (0,360) and reversing order of RA for plot
RAGal=ga.ra.wrap_at(180*u.deg).radian
DECGal=ga.dec.radian
RAGal=-RAGal
#plotting  galactic plane
plt.scatter(RAGal,DECGal,c='red',s=10,zorder=1,label="Glactic Plane")

#relabeling tickmarks to hours
ax.set_xticklabels(np.array(['10h', '8h','6h','4h', '2h','0h','22h','20h','18h','16h','14h']),color='k')
label="KMap.jpg"
plt.savefig(label,format='jpg',dpi=300)



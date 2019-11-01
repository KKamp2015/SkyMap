'''
Keefe Kamp
This code was made for SPS4010 Stellar Structues and Interiors.
This code produces a sky map of Be stars using an aitoff projection with included boxes for telescope range for SARA Telescopes
'''
# Improting the needed packages
import matplotlib.pyplot as plt # allows plot to be made
import numpy as np # allows for conversion between radians and degress and second method to read text in.
from astroquery.simbad import Simbad
from astropy.io import ascii
from astropy.coordinates import SkyCoord
import astropy.units as u

stars=ascii.read('B3.csv',delimiter=';',header_start=4,data_start=6,data_end=-1)

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
		cord=SkyCoord(stars['coord1 (ICRS,J2000/2000)'][i],unit=(u.deg, u.deg))
		Dec.append(cord.dec.deg)
		RA.append(cord.ra.deg)
	except:
		
		K+=1
print(K," not plotted")
x=np.array(RA)
#manipulating RA to be plot from -180 to 180
i=x>180# finding indecies above 180
x[i]-=360 #stubtracting 360 from RA<180 deg
x=-x

#making range boxs

ax.scatter(np.radians(x),np.radians(Dec),marker='*',s=1,color='k',label=None)

#relabeling tickmarks to hours
ax.set_xticklabels(np.array(['10h', '8h','6h','4h', '2h','0h','22h','20h','18h','16h','14h']),color='k')

label="B3Map.jpg"
plt.savefig(label,format='jpg',dpi=300)



'''
Keefe Kamp
This code was made for SPS4010 Stellar Structues and Interiors.
This code produces a sky map of Be stars using an aitoff projection with included boxes for telescope range for SARA Telescopes
'''
# Improting the needed packages
from astropy.io import ascii #allows files to be read
import matplotlib.pyplot as plt # allows plot to be made
import numpy as np # allows for conversion between radians and degress and second method to read text in.

i=0
while i==0:
	Obs=input("Which Observatory? KPN, RM, or CTIO ")
	if Obs=='KPN':
		DecH=89
		DecL=-40
		break
	if Obs=='RM':
		DecH=89
		DecL=-40
		break
	if Obs=='CTIO':
		DecH=38
		DecL=-89
		break
	else:
		i=0



RALi=input("Lower Limit for Hour Angle ")
RALi=float(RALi)
RAHi=input("Higher Limit for Hour Angle ")
RAHi=float(RAHi)
RAL=RALi*(360/24)
RAH=RAHi*(360/24)

stars=ascii.read('CoordBe.csv')

#Sets Global parameters 
plt.rc('axes', axisbelow=True)
#sets up plot
fig=plt.figure()#Creates plot
ax=fig.add_subplot(111,projection='aitoff')#puts plot into an Aitoff Projection
ax.grid(1)#turns grid lines on
#isolating Right Acsention(RA) array for manipulation

x=np.array(stars['RA'][:])

#manipulating RA to be plot from -180 to 180
i=x>180# finding indecies abouve 180
x[i]-=360 #stubtracting 360 from RA<180 deg
x=-x

#making range boxs

if RALi>iRAH:
	if RAL>180:
		RAL-=360
	if RAH>180:
		RAH-=360
	RAL*=-1
	RAH*=-1

	ax.fill(np.radians([RAH,180,180,RAH]),np.radians([DecH,DecH,DecL,DecL]),'r',alpha=.25)
	ax.fill(np.radians([-180,RAL,RAL,-180]),np.radians([DecH,DecH,DecL,DecL]),'r',alpha=.25)
else:
	

ax.scatter(np.radians(x[:]),np.radians(stars['DEC'][:]),marker='*',s=1,color='k',label=None)

#relabeling tickmarks to hours
ax.set_xticklabels(np.array(['10h', '8h','6h','4h', '2h','0h','22h','20h','18h','16h','14h']),color='k')

label='Map'+Obs+'RA'+str(RALi)+'to'+str(RAHi)+".jpg"
plt.savefig(label,format='jpg',dpi=300)



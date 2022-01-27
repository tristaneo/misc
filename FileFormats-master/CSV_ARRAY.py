import numpy as np

filename = 'sla.csv'
np.loadtxt(filename,delimiter=",", skiprows=1)
ds = np.loadtxt(filename,delimiter=",", skiprows=1)

i = 0
while i < len(ds):
	print("lon = "+str(ds[:,0][i])+", lat = "+str(ds[:,1][i])+", sla = "+str(ds[:,2][i])+", sla_sd = "+str(ds[:,3][i]))

	# regrid


    i += 1



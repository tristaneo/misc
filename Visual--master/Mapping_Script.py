import matplotlib.pyplot as plt
from cartopy.crs import PlateCarree
import xarray as xr
 
#read in data 

#ax = plt.subplot(111,projection=PlateCarree()) #sets 

#ds['LAI'].plot.imshow(ax=ax,cbar_kwargs={'orientation':'horizontal'},vmin=0,vmax=6)

import matplotlib.pyplot as plt

import cartopy.crs as ccrs


def main():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    ax.set_global()

    ax.stock_img()
    ax.coastlines()

    ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())

    plt.show()

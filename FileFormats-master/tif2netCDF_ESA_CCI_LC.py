import numpy as np
import sys
import xarray as xr #xarray to read all types of formats
from affine import Affine
#import useful


#load = sys.argv[4]#'new'
#Load the data

ds = xr.open_rasterio('sdat_1284_1_20190506_082415622_1.tif')[0]

# create netcdf file
# netcdf
# first deal with metadata and coordinates
tr = ds.attrs['transform']#Affine.from_gdal(*agb.attrs['transform'])
transform = Affine(tr[0],tr[1],tr[2],tr[3],tr[4],tr[5])
nx, ny = ds.sizes['x'], ds.sizes['y']
col,row = np.meshgrid(np.arange(nx)+0.5, np.arange(ny)+0.5)
lon, lat = transform * (col,row)

coords = {'lat': (['lat'],lat[:,0],{'units':'degrees_north','long_name':'latitude'}),
          'lon': (['lon'],lon[0,:],{'units':'degrees_east','long_name':'longitude'})}
attrs={'_FillValue':-9999.,'units':'none'}

data_vars = {}
data_vars['FloodedForestMask'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['Non_FloodedForestMask'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['Seasonal_FloodedForestMask'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['FloodedWoodlandMask'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['Non_WetlandMask'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)

ds_new = xr.Dataset(data_vars=data_vars,coords=coords)
ds_new.FloodedForestMask.values = ds.values == 99 #array1_to_go_here
ds_new.Non_FloodedForestMask.values = ds.values == 88 #array2_to_go_here
ds_new.Seasonal_FloodedForestMask.values = ds.values == 89
ds_new.FloodedWoodlandMask.values = ds.values == 77
ds_new.Non_WetlandMask.values = ds.values == 1
# combined woodland and forest



#save to a nc file
nc_file = 'LBA_Wetland_Extent_Processed_1x1.nc'
ds_new.to_netcdf(path=nc_file)

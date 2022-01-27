import numpy as np
import sys
import xarray as xr #xarray to read all types of formats
from affine import Affine
#import useful


#load = sys.argv[4]#'new'
#Load the data

ds = xr.open_rasterio('ESACCI-LC-2015_LAI_grid_compressed.tif')[0]

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
data_vars['All_Forest'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['All_Shrub'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['All_Grassland'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)
data_vars['Possible_Cerrado'] = (['lat','lon'],np.zeros([ny,nx])*np.nan,attrs)


ds_new = xr.Dataset(data_vars=data_vars,coords=coords)
ds_new.All_Forest.values = (ds.values>=50)*(ds.values<=90) #array1_to_go_here(lc>=50)*(lc<=90)
ds_new.All_Shrub.values = (ds.values>=120)*(ds.values<=122) #array2_to_go_here
ds_new.All_Grassland.values = ds.values == 130
ds_new.Possible_Cerrado.values = (ds.values>=150)*(ds.values<=153)

# combined woodland and forest



#save to a nc file
nc_file = 'ESA_LANDCOVER_GRID.nc'
ds_new.to_netcdf(path=nc_file)

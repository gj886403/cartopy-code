# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:26:36 2019

@author: qw919026
"""

from netCDF4 import Dataset, MFDataset, num2date
import matplotlib.pylab as plt
import numpy as np
from matplotlib import cm
import cartopy.crs as ccrs
from cmocean import cm as cmo
import sys
import os
from cartopy.util import add_cyclic_point

#Open the file and read in coordinates
flf = Dataset('C://Users//qw919026//Desktop//globalchange//temperature_annual_1deg.nc')
lat = flf.variables['lat'][:]
lon = flf.variables['lon'][:]

#Read in temperature from the first layer.
temp = flf.variables['t_an'][0,0,:,:]

#Make a basic cartopy plot
plt.figure(figsize=(13,6.2))
    
ax = plt.subplot(111, projection=ccrs.PlateCarree())

mm = ax.pcolormesh(lon,lat, temp, vmin=-2, vmax=30,\
                   transform=ccrs.PlateCarree(),cmap=cmo.thermal )
ax.coastlines()

#Get rid of line along 0 longitude
temp_cyc, lon_cyc = add_cyclic_point(temp, coord=lon)

plt.figure(figsize=(13,6.2))
    
ax = plt.subplot(111, projection=ccrs.PlateCarree())

mm = ax.pcolormesh(lon_cyc, lat, temp_cyc, vmin=-2, vmax=30,
transform=ccrs.PlateCarree(), cmap=cmo.balance )

ax.coastlines()

#use default cartopy backgroung
plt.figure(figsize=(13,6.2))
    
ax = plt.subplot(111, projection=ccrs.PlateCarree())

mm = ax.pcolormesh(lon_cyc, lat, temp_cyc, vmin=-2, vmax=30,
transform=ccrs.PlateCarree(), cmap=cmo.balance )

ax.coastlines()
ax.stock_img()


# Let's setup cartopy for use of the custom background. You have to have a folder that 
#contains background images and a json file that describes images.Then you have to
# create environment variable that contains the path to the folder:
os.environ["CARTOPY_USER_BACKGROUNDS"] = "/home/magik/PYTHON/cartopy/BG/"

#Now you can specify name of the image in it's resolution in the background_img() method:
#Example 1
plt.figure(figsize=(13,6.2))
    
ax = plt.subplot(111, projection=ccrs.PlateCarree())
ax.background_img(name='BM', resolution='low')
mm = ax.pcolormesh(lon_cyc,\
                   lat,\
                   temp_cyc,\
                   vmin=-2,\
                   vmax=30,\
                   transform=ccrs.PlateCarree(),\
                   cmap=cmo.balance )
ax.coastlines(resolution='110m')

#Example 2
plt.figure(figsize=(13,6.2))
    
ax = plt.subplot(111, projection=ccrs.Mercator(central_longitude=180, min_latitude=-30, max_latitude=67))
ax.background_img(name='BM', resolution='high')
ax.set_extent([30,-70,-30,70])
mm = ax.pcolormesh(lon,\
                   lat,\
                   temp,vmin=-2, vmax=30, transform=ccrs.PlateCarree(),cmap=cmo.balance )
ax.coastlines(resolution='10m')

#Example 3
plt.figure(figsize=(13,6.2))
    
ax = plt.subplot(111, projection=ccrs.Mercator(central_longitude=180, min_latitude=-30, max_latitude=67))
ax.background_img(name='pop', resolution='high')
ax.set_extent([30,-70,-30,70])
mm = ax.pcolormesh(lon,\
                   lat,\
                   temp,vmin=-2, vmax=30, transform=ccrs.PlateCarree(),cmap=cmo.balance )
ax.coastlines()






















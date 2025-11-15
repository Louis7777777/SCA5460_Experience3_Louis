#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
os.environ["NUMPY_EXPERIMENTAL_DTYPE_API"] = "1"
import matplotlib.pyplot as plt
import climlab
from climlab import constants as constants
import copy
import sys
import xarray as xr
ncep_url = "https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/"
ncep_air = xr.open_dataset( ncep_url + "pressure/air.mon.1981-2010.ltm.nc", decode_times=False)
level = ncep_air.level
lat = ncep_air.lat
Tzon = ncep_air.air.mean(dim=('lon','time'))
weight = np.cos(np.deg2rad(lat)) / np.cos(np.deg2rad(lat)).mean(dim='lat')
Tglobal = (Tzon * weight).mean(dim='lat')
np.save('ncep_lev.npy',Tglobal.level.values)
np.save('ncep_T.npy',Tglobal.values)

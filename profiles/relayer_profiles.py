#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy
import h5py


def interp_loz_81_13(pb81, loz81):

    p0 = 1013.25  # hPa

    # integrate profile to cumulative column
    coz81 = np.cumsum(loz81, axis=0)

    # generate umkehr pressure grid
    pb13 = np.exp(np.log(p0) - np.arange(13)*np.log(2))

    # ... and flip it
    pb13 = pb13[::-1]

    # create arrays to store umkehr profile
    coz13 = np.ndarray([13])
    loz13 = np.ndarray([13])

    # interpolate reversed cumulative profile from 81 to 13 layers
    xnew = np.log(pb13)
    x = np.log(pb81)
    y = np.log(coz81)

    coz13 = np.exp(np.interp(xnew, x, y))

    loz13[0] = coz13[0]

    for k in range(1, 13):
        loz13[k] = coz13[k] - coz13[k-1]

    return pb13, loz13


if __name__ == "__main__":


    filename = "/Users/dhaffner/DATA/o3_profile/MLS_GMI_SBUV_CLIM/SBUV_81_lyr_gmi_5deg.sav"
    data = scipy.io.readsav(filename)

    loz81 = data["loz81_5deg_gmi"]
    pb81 = data["pb81"]
    pb81 = pb81[:81]  # remove the extra level at N=82

    # flip profiles
    pb81_r = pb81[::-1]
    loz81_r = loz81[::-1]
    
    # create storage array for output profiles in 13 layers
    loz13_r = np.ndarray([13, 36, 12])

    # relayer profiles
    for j in range(36):
        for i in range(12):
            pb13_r, loz13_r[:, j, i] = interp_loz_81_13(pb81_r, loz81_r[:, j, i])

    # flip 13 layer grids back
    pb13 = pb13_r[::-1]
    loz13 = loz13_r[::-1,:,:]
    
    # confirm conservation of total ozone
    toz13 = np.sum(loz13,axis=0)
    toz81 = np.sum(loz81,axis=0)

    assert(np.max(toz13-toz81) < 1e-3)
    
    with h5py.File("SBUV_13_lyr_gmi_5deg_v3.h5", "w") as f:
        f["loz13_5deg_gmi"] = loz13
        f["pb13"] = pb13
        f["month"] = data["month"]
        f["lat"] = data["lat"]

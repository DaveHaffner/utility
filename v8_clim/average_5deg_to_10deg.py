import h5py
import numpy as np


with h5py.File("SBUV_13_lyr_gmi_5deg.h5", "r") as f_src:
    
    loz_36 = f_src["loz13_5deg_gmi"][...]
    lat_36 = f_src["lat"][...]
    
    loz_18 = np.ndarray([13, 18, 12])
    lat_18 = np.ndarray([18])
    
    for i in range(18):
        loz_18[:, i, :] = loz_36[:, 2*i, :] + loz_36[:, 2*i+1, :]
        lat_18[i] = lat_36[2*i] + lat_36[2*i+1]

    loz_18 /= 2.
    lat_18 /= 2.
    
    with h5py.File("SBUV_13_lyr_gmi_10deg.h5", "w") as f_dest:
        f_dest.copy(f_src["/month"], f_dest["/"])
        f_dest.copy(f_src["/pb13"], f_dest["/"])
        f_dest["lat"] = lat_18
        f_dest["loz13_10deg_gmi"] = loz_18

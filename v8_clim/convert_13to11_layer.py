import numpy as np
import h5py

filename = "/Users/dhaffner/project/omi_to3_v85c4_alg1/data/final/SBUV_13_lyr_gmi_10deg.h5"

with h5py.File(filename, "r") as f:
    loz13 = f["loz13_10deg_gmi"][...]
    loz11 = np.ndarray([11, 18, 12])
    loz11[0:10, :, :] = loz13[0:10, :, :]
    loz11[10, :, :] = loz13[10, :, :] + loz13[11, :, :] + loz13[12, :, :]
    pb13 = f["pb13"][...]
    pb11 = pb13[0:11]
    month = f["month"][...]
    lat = f["lat"][...]

with h5py.File("SBUV_11_lyr_gmi_10deg.h5", "w") as f:
    f["lat"] = lat
    f["month"] = month
    f["pb11"] = pb11
    f["loz11_10deg_gmi"] = loz11

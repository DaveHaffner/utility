import numpy as np
import numpy.typing as npt


def umkehr_grid(num_layers: int) -> npt.ArrayLike:
    """Generate Umkehr pressure level grid

    The Umkehr pressure level grid halves the pressure P of the next
    atmospheric level (dlog P = log(2)) for each level from bottom to
    top of the atmosphere.

    This function generates an Umkehr grid with any number of pressure
    levels N specified, however in practice the number of levels is
    usually 11 or 13.

    Parameters
    ----------
    num_layers : int
        Number of layers

    Returns
    -------
    pressure_grid: np.ndarray

    Example
    -------
    Compute Umkehr grid with 13 levels.

    >>> umkehr_grid(13)

    array([1.01325000e+03, 5.06625000e+02, 2.53312500e+02, 1.26656250e+02,
           6.33281250e+01, 3.16640625e+01, 1.58320313e+01, 7.91601563e+00,
           3.95800781e+00, 1.97900391e+00, 9.89501953e-01, 4.94750977e-01,
           2.47375488e-01])

    """
    p0 = 1013.25
    dlogp = np.log(2.)
    logp = np.log(p0)-np.arange(num_layers)*dlogp
    p = np.exp(logp)
    return p


def decade_grid(num_layers: int, num_layers_per_decade: int) -> npt.ArrayLike:
    """Generate pressure level grid with fixed number of layers per
    decade in pressure (dlog10 P is 1/num_layers_per_decade

    Parameters
    ----------
    num_layers : int
        Number of layers

    num_layers_per_decade : int
        Number of layers per decade

    Returns
    -------
    pressure_grid: np.ndarray

    Example
    -------
    Compute 101 layer grid with 20 layers per decade

    >>> decade_grid(101,20)

    array([1.01325000e+03, 9.03060013e+02, 8.04853084e+02, 7.17326066e+02,
           6.39317529e+02, 5.69792348e+02, 5.07827964e+02, 4.52602150e+02,
           4.03382091e+02, 3.59514667e+02, 3.20417784e+02, 2.85572651e+02,
           2.54516893e+02, 2.26838419e+02, 2.02169954e+02, 1.80184161e+02,
           1.60589303e+02, 1.43125367e+02, 1.27560617e+02, 1.13688520e+02,
           1.01325000e+02, 9.03060013e+01, 8.04853084e+01, 7.17326066e+01,
           6.39317529e+01, 5.69792348e+01, 5.07827964e+01, 4.52602150e+01,
           4.03382091e+01, 3.59514667e+01, 3.20417784e+01, 2.85572651e+01,
           2.54516893e+01, 2.26838419e+01, 2.02169954e+01, 1.80184161e+01,
           1.60589303e+01, 1.43125367e+01, 1.27560617e+01, 1.13688520e+01,
           1.01325000e+01, 9.03060013e+00, 8.04853084e+00, 7.17326066e+00,
           6.39317529e+00, 5.69792348e+00, 5.07827964e+00, 4.52602150e+00,
           4.03382091e+00, 3.59514667e+00, 3.20417784e+00, 2.85572651e+00,
           2.54516893e+00, 2.26838419e+00, 2.02169954e+00, 1.80184161e+00,
           1.60589303e+00, 1.43125367e+00, 1.27560617e+00, 1.13688520e+00,
           1.01325000e+00, 9.03060013e-01, 8.04853084e-01, 7.17326066e-01,
           6.39317529e-01, 5.69792348e-01, 5.07827964e-01, 4.52602150e-01,
           4.03382091e-01, 3.59514667e-01, 3.20417784e-01, 2.85572651e-01,
           2.54516893e-01, 2.26838419e-01, 2.02169954e-01, 1.80184161e-01,
           1.60589303e-01, 1.43125367e-01, 1.27560617e-01, 1.13688520e-01,
           1.01325000e-01, 9.03060013e-02, 8.04853084e-02, 7.17326066e-02,
           6.39317529e-02, 5.69792348e-02, 5.07827964e-02, 4.52602150e-02,
           4.03382091e-02, 3.59514667e-02, 3.20417784e-02, 2.85572651e-02,
           2.54516893e-02, 2.26838419e-02, 2.02169954e-02, 1.80184161e-02,
           1.60589303e-02, 1.43125367e-02, 1.27560617e-02, 1.13688520e-02,
           1.01325000e-02])
    """

    p0 = 1013.25
    dlogp = 1./num_layers_per_decade
    logp = np.log10(p0)-np.arange(num_layers)*dlogp
    p = 10.**logp
    return p

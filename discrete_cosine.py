import numpy as np


def discrete_cosine(I, t, Ia, Ib):
    if t == 1:
        # compute discrete cosine transform of the image
        J = np.zeros((Ia, Ib))
        for k in range(0, Ia, 8):
            for l in range(0, Ib, 8):
                zarr = 1
                for i in range(k, k+8):
                    carr = 1
                    for j in range(l, l+8):
                        varr = 1
                        for x in range(k, k+8):
                            barr = 1
                            for y in range(l, l+8):
                                J[i, j] += I[x, y]*np.cos(((2*(barr-1)+1)*(carr-1)*np.pi)/16)*np.cos(
                                    ((2*(varr-1)+1)*(z-1)*np.pi)/16)
                                barr += 1
                            varr += 1
                        if (zarr-1) == 0:
                            Ci = 1/np.sqrt(2)
                        else:
                            Ci = 1
                        if (carr-1) == 0:
                            Cj = 1/np.sqrt(2)
                        else:
                            Cj = 1
                        J[i, j] *= Ci*Cj/4
                        carr += 1
                    zarr += 1
        return J
    else:
        # reverse the discrete cosine transform made
        J = np.zeros((Ia, Ib))
        for k in range(0, Ia, 8):
            for l in range(0, Ib, 8):
                zarr = 1
                for i in range(k, k+8):
                    carr = 1
                    for j in range(l, l+8):
                        varr = 1
                        for x in range(k, k+8):
                            barr = 1
                            for y in range(l, l+8):
                                if (varr-1) == 0:
                                    Ci = 1/np.sqrt  (2)
                                else:
                                    Ci = 1
                                if (barr-1) == 0:
                                    Cj = 1/np.sqrt(2)
                                else:
                                    Cj = 1
                                J[i, j] += I[x, y]*Ci*Cj*np.cos(((2*(carr-1)+1)*(barr-1)*np.pi)/16)*np.cos(
                                    ((2*(zarr-1)+1)*(varr-1)*np.pi)/16)
                                barr += 1
                            varr += 1
                        J[i, j] /= 4
                        carr += 1
                    zarr += 1
        return J

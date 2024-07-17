import numpy as np
import matplotlib.pyplot as plt

def soft_sand_wet(n, Vclay, phi, P):
    phic = 0.4
    Kc = 36.6e9  # quartz bulk modulus, Pa
    Gc = 45e9  # quartz shear modulus, Pa
    Mc = Kc + Gc * (4 / 3)  # quartz compressional modulus
    Dc = 2.65  # quartz density
    Prc = 0.06  # quartz Poisson's ratio
    K_clay = 21e9  # clay bulk modulus, Pa
    G_clay = 7e9  # clay shear modulus, Pa
    D_clay = 2.58  # clay density
    Pr_clay = 0.35  # clay Poisson's ratio
    f = 0.5  # fraction of contacts in Hertz-Mindlin equation

    Ds = Dc * (1 - Vclay) + D_clay * Vclay  # Solid phase density

    Kv = Kc * (1 - Vclay) + K_clay * Vclay
    Kr = ((1 - Vclay) / Kc + Vclay / K_clay) ** -1
    Kh = (Kv + Kr) / 2
    K = Kh  # Solid grain

    Gv = Gc * (1 - Vclay) + G_clay * Vclay
    Gr = ((1 - Vclay) / Gc + Vclay / G_clay) ** -1
    Gh = (Gv + Gr) / 2
    G = Gh  # Solid grain

    Khm = (n ** 2 * (1 - phic) ** 2 * G ** 2 * P / (18 * np.pi ** 2 * (1 - Pr_clay) ** 2)) ** (1 / 3)
    Ghm = ((5 - 4 * Pr_clay) / (5 * (2 - Pr_clay))) * (3 * n ** 2 * (1 - phic) ** 2 * G ** 2 * P / (2 * np.pi ** 2 * (1 - Pr_clay) ** 2)) ** (1 / 3)

    Ksoft = ((phi / phic) / (Khm + 4 / 3 * Ghm) + (1 - phi / phic) / (K + 4 / 3 * Ghm)) ** -1 - 4 / 3 * Ghm
    Zhm = (Ghm / 6) * (9 * Khm + 8 * Ghm) / (Khm + 2 * Ghm)
    Gsoft = ((phi / phic) / (Ghm + Zhm) + (1 - phi / phic) / (G + Zhm)) ** -1 - Zhm

    Ks = K  # Solid grain K
    Kframe = Ksoft  # Dry rock K
    Kf = 2.68e9  # Water K, in Pa
    Df = 1.03  # Water Density

    # Gassmann Dry K to Sat K
    Ksat = Ks * (phi * Kframe - (1 + phi) * Kf * Kframe / Ks + Kf) / ((1 - phi) * Kf + phi * Ks - Kf * Kframe / Ks)

    Ksoft = Ksat / 1e9
    Gsoft = Gsoft / 1e9
    Db = Ds * (1 - phi) + Df * phi

    vp = np.sqrt((Ksoft + Gsoft * 4 / 3) / Db) * 1000
    vs = np.sqrt(Gsoft / Db) * 1000

    return vp, vs, Ksoft, Gsoft

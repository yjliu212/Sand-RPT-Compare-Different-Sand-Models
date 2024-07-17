import numpy as np
import matplotlib.pyplot as plt

def contact_cement_wet(n, Vclay, phi):
    phic = 0.4
    Kc = 36.6  # quartz bulk modulus
    Gc = 45  # quartz shear modulus
    Mc = Kc + Gc * (4 / 3)  # quartz compressional modulus
    Dc = 2.65  # quartz density
    Prc = 0.06  # quartz Poisson's ratio
    K_clay = 21  # clay bulk modulus
    G_clay = 7  # clay shear modulus
    D_clay = 2.58  # clay density
    Pr_clay = 0.35  # clay Poisson's ratio

    Ds = Dc * (1 - Vclay) + D_clay * Vclay  # Solid phase density

    Kv = Kc * (1 - Vclay) + K_clay * Vclay
    Kr = ((1 - Vclay) / Kc + Vclay / K_clay) ** -1
    Kh = (Kv + Kr) / 2
    K = Kh

    Gv = Gc * (1 - Vclay) + G_clay * Vclay
    Gr = ((1 - Vclay) / Gc + Vclay / G_clay) ** -1
    Gh = (Gv + Gr) / 2
    G = Gh

    alpha = (2 * (phic - phi) / (3 * (1 - phic))) ** 0.5
    At = Gc / (np.pi * G)
    An = (2 * Gc / (np.pi * G)) * ((1 - Pr_clay) * (1 - Prc) / (1 - 2 * Prc))

    Ct = 10 ** -4 * (9.654 * Pr_clay ** 2 + 4.945 * Pr_clay + 3.1) * At ** (0.01867 * Pr_clay ** 2 + 0.4011 * Pr_clay - 1.8186)
    Bt = (0.0573 * Pr_clay ** 2 + 0.0937 * Pr_clay + 0.202) * At ** (0.0274 * Pr_clay ** 2 + 0.0529 * Pr_clay - 0.8765)
    AAt = -10 ** -2 * (2.26 * Pr_clay ** 2 + 2.07 * Pr_clay + 2.3) * At ** (0.079 * Pr_clay ** 2 + 0.1754 * Pr_clay - 1.342)
    St = AAt * alpha ** 2 + Bt * alpha + Ct

    Cn = 0.00024649 * An ** -1.9864
    Bn = 0.20405 * An ** -0.89008
    AAn = -0.024153 * An ** -1.3646
    Sn = AAn * alpha ** 2 + Bn * alpha + Cn

    Kcem = (1 / 6) * n * (1 - phic) * Mc * Sn
    Gcem = (3 / 5) * Kcem + (3 / 20) * n * (1 - phic) * Gc * St

    Ks = K  # Solid grain K
    Kframe = Kcem  # Dry rock K
    Kf = 2.68  # Water K
    Df = 1.03  # Water Density

    # Gassmann Dry K to Sat K
    Ksat = Ks * (phi * Kframe - (1 + phi) * Kf * Kframe / Ks + Kf) / ((1 - phi) * Kf + phi * Ks - Kf * Kframe / Ks)

    Kcem = Ksat
    Gcem = Gcem
    Db = Ds * (1 - phi) + Df * phi

    vp = np.sqrt((Kcem + Gcem * 4 / 3) / Db) * 1000
    vs = np.sqrt(Gcem / Db) * 1000

    return vp, vs, Kcem, Gcem

# Example usage
#n = 6
#Vclay = 0.1
#phi = np.linspace(0, 0.4, 100)

#vp, vs, Kcem, Gcem = contact_cement_wet(n, Vclay, phi)

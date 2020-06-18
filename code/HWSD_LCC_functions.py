# function to assign USDA texture class in string format to numeric classes from HWSD dataset
# apply to T_USDA_TEX column and S_USDA_TEX column
def inttex_to_stringtex(USDA_tex):
    switcher = {
        1: "clay",
        2: "silty clay",
        3: "clay",
        4: "silty clay loam",
        5: "clay loam",
        6: "silt",
        7: "silt loam",
        8: "sandy clay",
        9: "loam",
        10: "sandy clay loam",
        11: "sandy loam",
        12: "loamy sand",
        13: "sand"
    }
    return switcher.get(USDA_tex, "err")


# function to calculate erosion risk LCC class
# calculates K factor and combines with slope to determine risk
def erosion_risk_LCC(row):
    texture = row["T_USDA_TEX"]
    slope = row['slope']
    erosion_risk_lcc = 1

    # first calculate k factor based on texture
    list1 = ["loam", "silt loam", "silt"]
    if list1.count(texture) > 0:
        k_fac = .33
    else:
        k_fac = .31

    # then calculate lcc class of erosion risk combining k factor and slope
    if k_fac > .32 and slope <= 2:
        erosion_risk_lcc = 1
    elif k_fac > .32 and (slope > 2 and slope <= 5):
        erosion_risk_lcc = 2
    elif k_fac > .32 and (slope > 5 and slope <= 10):
        erosion_risk_lcc = 3
    elif k_fac > .32 and (slope > 10 and slope <= 15):
        erosion_risk_lcc = 4
    elif k_fac > .32 and (slope > 15 and slope <= 30):
        erosion_risk_lcc = 6
    elif k_fac > .32 and (slope > 30 and slope <= 60):
        erosion_risk_lcc = 7
    elif k_fac > .32 and slope > 60:
        erosion_risk_lcc = 8
    elif k_fac <= 0.32 and slope <= 5:
        erosion_risk_lcc = 1
    elif k_fac <= 0.32 and (slope > 5 and slope <= 10):
        erosion_risk_lcc = 2
    elif k_fac <= 0.32 and (slope > 10 and slope <= 15):
        erosion_risk_lcc = 3
    elif k_fac <= 0.32 and (slope > 15 and slope <= 30):
        erosion_risk_lcc = 4
    elif k_fac <= 0.32 and (slope > 30 and slope <= 60):
        erosion_risk_lcc = 7
    elif k_fac <= 0.32 and slope > 60:
        erosion_risk_lcc = 8
    else:
        erosion_risk_lcc = 'err'

    return erosion_risk_lcc


# function to calculate surface soil texture LCC class
# takes in texture and outputs LCC class
def soil_tex_LCC(row):
    texture = row["T_USDA_TEX"]
    list1 = ["sandy loam", "silt loam", "loam", "silt", "sandy clay loam", "silty clay loam", "clay loam"]
    list2 = ["sand", "loamy sand", "sandy clay", "silty clay"]
    surface_st_lcc = 1

    if list1.count(texture) > 0:
        surface_st_lcc = 1
    elif list2.count(texture) > 0:
        surface_st_lcc = 2
    elif texture == "clay":
        surface_st_lcc = 3
    else:
        surface_st_lcc = 1

    return surface_st_lcc


#  function to calculate soil depth LCC class
#  takes in phases and outputs LCC class if lithic phase is present
def depth_LCC(row):
    phase1 = row["PHASE1"]
    phase2 = row["PHASE2"]
    roots = row['ROOTS']
    depth_LCC = 1
    if phase1 == 2 or phase2 == 2:
        depth_LCC = 6
    elif phase1 in [4, 5, 6, 8, 9, 17] or phase2 in [4, 5, 6, 8, 9, 17]:
        depth_LCC = 4
    elif roots == 2:
        depth_LCC = 3
    elif roots == 3:
        depth_LCC = 4
    elif roots in [4, 5]:
        depth_LCC = 6
    elif roots == 6:
        depth_LCC = 8
    else:
        depth_LCC = 1

    return depth_LCC


# function to calculate salinity LCC class
# takes in T_ECE and outputs LCC class
def salinity_LCC(row):
    salinity_lcc = 1
    t_ece = row['T_ECE']
    if t_ece < 2:
        salinity_lcc = 1
    elif t_ece >= 2 and t_ece <= 4:
        salinity_lcc = 2
    elif t_ece > 4 and t_ece <= 8:
        salinity_lcc = 3
    elif t_ece > 8 and t_ece <= 16:
        salinity_lcc = 4
    elif t_ece > 16 and t_ece <= 30:
        salinity_lcc = 6
    elif t_ece > 30 and t_ece <= 40:
        salinity_lcc = 7
    elif t_ece > 40:
        salinity_lcc = 8

    return salinity_lcc


# function to calculate flooding LCC class
# takes in phases and flags for inundic phase
def flooding_LCC(row):
    flood = 1
    phase1 = row["PHASE1"]
    phase2 = row["PHASE2"]

    if phase1 == 16 or phase2 == 16:
        flood = 4
    else:
        flood = 1

    return (flood)


def surface_stoniness_LCC(row):
    phase1 = row["PHASE1"]
    phase2 = row["PHASE2"]
    stone = row['T_GRAVEL']
    stone_LCC = 1
    if phase1 == 18 or phase2 == 18:
        stone_LCC = 5
    else:
        if stone < .1:
            stone_LCC = 1
        elif stone >= .1 and stone < 3:
            stone_LCC = 2
        elif stone >= 3 and stone < 15:
            stone_LCC = 3
        elif stone >= 15 and stone < 50:
            stone_LCC = 5
        elif stone >= 50 and stone < 90:
            stone_LCC = 7
        elif stone >= 90:
            stone_LCC = 8

    return (stone_LCC)


# function to calculate lime requirement LCC class
# takes in T_PH_H2O and outputs LCC class
def lime_LCC(row):
    lime_lcc = 1
    ph_val = row["T_PH_H2O"]
    if ph_val >= 5.5 and ph_val <= 7.2:
        lime_lcc = 1
    elif (ph_val < 5.5 and ph_val >= 4.5) or (ph_val > 7.2 and ph_val <= 8.4):
        lime_lcc = 3
    elif ph_val < 4.5 or ph_val > 8.5:
        lime_lcc = 4

    return lime_lcc


# function to calculate permeability LCC class
# take in texture, calculate intermediary values, outpus LCC class
# based on landPKs alculation of permeability
def perm_LCC(row):
    import math
    tsand = row["T_SAND"] / 100
    tsilt = row['T_SILT'] / 100
    tclay = row['T_CLAY'] / 100
    tom = 2.17 * row['T_OC'] / 100
    tgravel = row['T_GRAVEL'] / 100

    ssand = row["S_SAND"] / 100
    ssilt = row['S_SILT'] / 100
    sclay = row['S_CLAY'] / 100
    som = 2.17 * row['S_OC'] / 100
    sgravel = row['S_GRAVEL'] / 100

    tWP1 = -0.024 * (tsand) + 0.487 * (tclay) + 0.006 * (tom) + 0.005 * (tsand) * (tom) - 0.013 * (tclay) * (
        tom) + 0.068 * (tsand) * (tclay) + 0.031
    tWP = tWP1 + (0.14 * tWP1 - 0.02)
    tFC1 = -0.251 * (tsand) + 0.195 * (tclay) + 0.011 * (tom) + 0.006 * (tsand) * (tom) - 0.027 * (tclay) * (
        tom) + 0.452 * (tsand) * (tclay) + 0.299
    tFC = tFC1 + (1.283 * tFC1 * tFC1 - 0.374 * tFC1 - 0.015)
    tLAWC = (tFC - tWP) * (1 - (tgravel))
    tSFC1 = 0.278 * (tsand) + 0.034 * (tclay) + 0.022 * (tom) - 0.018 * (tsand) * (tom) - 0.027 * (tclay) * (
        tom) - 0.584 * (tsand) * (tclay) + 0.078
    tSFC = tSFC1 + ((0.636 * tSFC1) - 0.107)
    tSASC = tFC + tSFC - 0.097 * (tsand) + 0.043
    tMSD = (1 - tSASC) * 2.65
    tBSD = (1 - (tgravel)) / (1 - (tgravel) * (1 - 1.5 * (tMSD / 2.65)))
    tL = (math.log(tWP) - math.log(tFC)) / (math.log(1500) - math.log(33))
    tKS = 1930 * (tSASC) ** (3 - tL) * tBSD

    sWP1 = -0.024 * (ssand) + 0.487 * (sclay) + 0.006 * (som) + 0.005 * (ssand) * (som) - 0.013 * (sclay) * (
        som) + 0.068 * (ssand) * (sclay) + 0.031
    sWP = sWP1 + (0.14 * sWP1 - 0.02)
    sFC1 = -0.251 * (ssand) + 0.195 * (sclay) + 0.011 * (som) + 0.006 * (ssand) * (som) - 0.027 * (sclay) * (
        som) + 0.452 * (ssand) * (sclay) + 0.299
    sFC = sFC1 + (1.283 * sFC1 * sFC1 - 0.374 * sFC1 - 0.015)
    sLAWC = (sFC - sWP) * (1 - (sgravel))
    sSFC1 = 0.278 * (ssand) + 0.034 * (sclay) + 0.022 * (som) - 0.018 * (ssand) * (som) - 0.027 * (sclay) * (
        som) - 0.584 * (ssand) * (sclay) + 0.078
    sSFC = sSFC1 + ((0.636 * sSFC1) - 0.107)
    sSASC = sFC + sSFC - 0.097 * (ssand) + 0.043
    sMSD = (1 - sSASC) * 2.65
    sBSD = (1 - (sgravel)) / (1 - (sgravel) * (1 - 1.5 * (sMSD / 2.65)))
    sL = (math.log(sWP) - math.log(sFC)) / (math.log(1500) - math.log(33))
    sKS = 1930 * (sSASC) ** (3 - sL) * sBSD

    min_KS = min(tKS, sKS)

    perm_lcc = 1
    if min_KS < 1.5:
        perm_lcc = 3
    elif min_KS >= 1.5 and min_KS <= 5:
        perm_lcc = 2
    elif min_KS > 5:
        perm_lcc = 1

    return perm_lcc


# function to calculate permeability LCC class
# take in texture, calculate intermediary values, outpus LCC class
# based on landPKs alculation of permeability
def LAWC_T(row):
    sand = row["T_SAND"] / 100
    silt = row["T_SILT"] / 100
    clay = row["T_CLAY"] / 100
    om = 2.17 * row["T_OC"] / 100
    gravel = row["T_GRAVEL"] / 100

    WP1 = -0.024 * (sand) + 0.487 * (clay) + 0.006 * (om) + 0.005 * (sand) * (om) - 0.013 * (clay) * (om) + 0.068 * (
        sand) * (clay) + 0.031
    WP = WP1 + (0.14 * WP1 - 0.02)
    FC1 = -0.251 * (sand) + 0.195 * (clay) + 0.011 * (om) + 0.006 * (sand) * (om) - 0.027 * (clay) * (om) + 0.452 * (
        sand) * (clay) + 0.299
    FC = FC1 + (1.283 * FC1 * FC1 - 0.374 * FC1 - 0.015)
    LAWC = (FC - WP) * (1 - (gravel))
    # MULTIPLY BY DEPTH OF SOIL HERE
    AWC = LAWC

    return AWC


def LAWC_S(row):
    sand = row["S_SAND"] / 100
    silt = row["S_SILT"] / 100
    clay = row["S_CLAY"] / 100
    om = 2.17 * row["S_OC"] / 100
    gravel = row["S_GRAVEL"] / 100

    WP1 = -0.024 * (sand) + 0.487 * (clay) + 0.006 * (om) + 0.005 * (sand) * (om) - 0.013 * (clay) * (om) + 0.068 * (
        sand) * (clay) + 0.031
    WP = WP1 + (0.14 * WP1 - 0.02)
    FC1 = -0.251 * (sand) + 0.195 * (clay) + 0.011 * (om) + 0.006 * (sand) * (om) - 0.027 * (clay) * (om) + 0.452 * (
        sand) * (clay) + 0.299
    FC = FC1 + (1.283 * FC1 * FC1 - 0.374 * FC1 - 0.015)
    LAWC = (FC - WP) * (1 - (gravel))
    AWC = LAWC

    return AWC


def AWC_LCC(row):
    Tawc = row["T_AWC"] * 30
    Sawc = row["S_AWC"] * 70

    AWC = Tawc + Sawc
    awc_lcc = 1
    if AWC > 18:
        awc_lcc = 1
    elif AWC > 12 and AWC <= 18:
        awc_lcc = 2
    elif AWC > 6 and AWC <= 12:
        awc_lcc = 3
    elif AWC <= 6:
        awc_lcc = 4
    else:
        awc_lcc = 0

    return awc_lcc


# function to calculate overall LCC
# input one row of the dataframe, to be applied to the full dataframe
def calc_LCC(row):
    lcc_final = max(row["erosion_risk_LCC"], row["soil_tex_LCC"], row["flooding_LCC"], row["surface_stoniness_LCC"],
                    row["depth_LCC"], row["salinity_LCC"],
                    row["lime_LCC"], row["perm_LCC"], row["awc_LCC"])

    return lcc_final


# function to calculate overall LCC
# input one row of the dataframe, to be applied to the full dataframe
def calc_LCC_noawc(row):
    lcc_final = max(row["erosion_risk_LCC"], row["soil_tex_LCC"], row["flooding_LCC"], row["surface_stoniness_LCC"],
                    row["depth_LCC"], row["salinity_LCC"],
                    row["lime_LCC"], row["perm_LCC"])

    return lcc_final


def limitation(row):
    LCC_final = row['LCC_final']
    erosion = row['erosion_risk_LCC']
    tex = row['soil_tex_LCC']
    perm = row['perm_LCC']
    awc = row['awc_LCC']
    lime = row['lime_LCC']
    depth = row['depth_LCC']
    salinity = row['salinity_LCC']
    stone = row['surface_stoniness_LCC']
    flood = row['flooding_LCC']

    lim = str(LCC_final)
    if erosion == LCC_final:
        lim += "e"
    if tex == LCC_final:
        lim += "s-t"
    if perm == LCC_final:
        lim += "w-p"
    if awc == LCC_final:
        lim += "s-a"
    if lime == LCC_final:
        lim += "s-l"
    if depth == LCC_final:
        lim += "s-d"
    if salinity == LCC_final:
        lim += "s-k"
    if stone == LCC_final:
        lim += "s-r"
    if flood == LCC_final:
        lim += "w-f"

    return (lim)


def limitation_noawc(row):
    LCC_final = row['LCC_final_noawc']
    erosion = row['erosion_risk_LCC']
    tex = row['soil_tex_LCC']
    perm = row['perm_LCC']
    lime = row['lime_LCC']
    depth = row['depth_LCC']
    salinity = row['salinity_LCC']
    stone = row['surface_stoniness_LCC']
    flood = row['flooding_LCC']

    lim = str(LCC_final)
    if erosion == LCC_final:
        lim += "e"
    if tex == LCC_final:
        lim += "s-t"
    if perm == LCC_final:
        lim += "w-p"
    if lime == LCC_final:
        lim += "s-l"
    if depth == LCC_final:
        lim += "s-d"
    if salinity == LCC_final:
        lim += "s-k"
    if stone == LCC_final:
        lim += "s-r"
    if flood == LCC_final:
        lim += "w-f"

    return (lim)
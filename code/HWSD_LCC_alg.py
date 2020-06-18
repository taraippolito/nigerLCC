# HWSD LCC calculation algorithm
# run for each partition

# Import packages and dependencies
import numpy as np
import pandas as pd
import math
from simpledbf import Dbf5
from HWSD_LCC_functions import inttex_to_stringtex, erosion_risk_LCC, soil_tex_LCC, flooding_LCC, surface_stoniness_LCC, depth_LCC, salinity_LCC, lime_LCC, perm_LCC, LAWC_T, LAWC_S, AWC_LCC, calc_LCC, calc_LCC_noawc, limitation, limitation_noawc

join_data = "D:\Tara_Fall_2019\dosso_index\\HWSd_dosso_la.dbf"
join_dbf = Dbf5(join_data)
df_join = join_dbf.to_dataframe()

# iterate over all partitions in the dosso region
for i in range(1):
    # import dataframes
    data0 = "D:\Tara_Fall_2019\dosso_index\\base_HWSD_slope" + str(i) + ".dbf"
    dbf0 = Dbf5(data0)
    df_data0 = dbf0.to_dataframe()

    # merge with full HWSD information
    df0 = df_data0.merge(df_join, on='OBJECTID', how="left")

    # pull texture from HWSD classes
    df0['T_USDA_TEX'] = df0['T_USDA_TEX'].apply(inttex_to_stringtex)

    # changing columns to be used in calculations
    df0['slope'] = df0['GRIDCODE'] / 10000

    # calculate LCC for subclasses
    df0["erosion_risk_LCC"] = df0.apply(erosion_risk_LCC, axis=1)
    df0["soil_tex_LCC"] = df0.apply(soil_tex_LCC, axis=1)
    df0["flooding_LCC"] = df0.apply(flooding_LCC, axis=1)
    df0["surface_stoniness_LCC"] = df0.apply(surface_stoniness_LCC, axis=1)
    df0["depth_LCC"] = df0.apply(depth_LCC, axis=1)
    df0["salinity_LCC"] = df0.apply(salinity_LCC, axis=1)
    df0["lime_LCC"] = df0.apply(lime_LCC, axis=1)
    df0["perm_LCC"] = df0.apply(perm_LCC, axis=1)
    df0["T_AWC"] = df0.apply(LAWC_T, axis=1)
    df0["S_AWC"] = df0.apply(LAWC_S, axis=1)
    df0['awc_LCC'] = df0.apply(AWC_LCC, axis=1)

    df0["LCC_final"] = df0.apply(calc_LCC, axis=1)
    df0["LCC_final_noawc"] = df0.apply(calc_LCC_noawc, axis=1)
    df0["limitation"] = df0.apply(limitation, axis=1)
    df0["limitation_noawc"] = df0.apply(limitation_noawc, axis=1)

    # make a succinct dataframe to be saved
    df0_succinct = df0[[
        'MU_GLOBAL', 'SHARE', 'SEQ',
        'SU_SYM74', 'SU_CODE74',
        'T_USDA_TEX',
         'S_USDA_TEX',
         'slope', 'erosion_risk_LCC', 'soil_tex_LCC',
        'flooding_LCC', 'surface_stoniness_LCC', 'depth_LCC', 'salinity_LCC',
        'lime_LCC', 'perm_LCC', 'T_AWC', 'S_AWC', 'awc_LCC', 'flood_LCC',
        'LCC_final', 'LCC_final_noawc', 'limitation', 'limitation_noawc']].copy()

    output_file = "LCC_HWSD_dosso_fullresults_" + str(i)

    df0_succinct.to_csv(output_file)

    print (str(i) + " completed!")






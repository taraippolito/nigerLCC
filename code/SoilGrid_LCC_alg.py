# SoilGrids LCC calculation algorithm
# to be run on 6 horizons : 0cm, 5cm, 15cm, 30cm, 60cm, 100cm
# run for each partition

# Import packages and dependencies
import numpy as np
import pandas as pd
import math
from simpledbf import Dbf5
from SoilGrid_LCC_functions import surf_texture, top_texture, awc1, awc2, awc3, awc4, awc5, erosion_risk_LCC, soil_tex_LCC, soil_tex_LCC, stoniness_LCC, perm_LCC, LAWC_LCC, lime_LCC, calc_LCC, calc_LCC_no_awc, limitation, limitation_noawc

#iterate over all 347 partitions of the dosso region
for i in range(1):
    # import datasets from all horizons for a given partition
    d01 = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_SG0_slope" + str(i) + ".dbf"
    d02 = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_SG5_join" + str(i) + ".dbf"
    d03 = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_SG15_join" + str(i) + ".dbf"
    d04 = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_SG30_join" + str(i) + ".dbf"
    d05 = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_SG60_join" + str(i) + ".dbf"
    d06 = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_SG100_join" + str(i) + ".dbf"

    # convert to pandas dataframes
    dbf01 = Dbf5(d01)
    dbf02 = Dbf5(d02)
    dbf03 = Dbf5(d03)
    dbf04 = Dbf5(d04)
    dbf05 = Dbf5(d05)
    dbf06 = Dbf5(d06)

    df01 = dbf01.to_dataframe()
    df02 = dbf02.to_dataframe()
    df03 = dbf03.to_dataframe()
    df04 = dbf04.to_dataframe()
    df05 = dbf05.to_dataframe()
    df06 = dbf06.to_dataframe()

    # normalize texture percentages
    df01['total_p'] = df01['sand'] + df01['silt'] + df01['clay']
    df02['total_p'] = df02['sand'] + df02['silt'] + df02['clay']
    df03['total_p'] = df03['sand'] + df03['silt'] + df03['clay']
    df04['total_p'] = df04['sand'] + df04['silt'] + df04['clay']
    df05['total_p'] = df05['sand'] + df05['silt'] + df05['clay']
    df06['total_p'] = df06['sand'] + df06['silt'] + df06['clay']

    df01['sand'] = df01['sand'] / df01['total_p']
    df02['sand'] = df02['sand'] / df02['total_p']
    df03['sand'] = df03['sand'] / df03['total_p']
    df04['sand'] = df04['sand'] / df04['total_p']
    df05['sand'] = df05['sand'] / df05['total_p']
    df06['sand'] = df06['sand'] / df06['total_p']

    df01['silt'] = df01['silt'] / df01['total_p']
    df02['silt'] = df02['silt'] / df02['total_p']
    df03['silt'] = df03['silt'] / df03['total_p']
    df04['silt'] = df04['silt'] / df04['total_p']
    df05['silt'] = df05['silt'] / df05['total_p']
    df06['silt'] = df06['silt'] / df06['total_p']

    df01['clay'] = df01['clay'] / df01['total_p']
    df02['clay'] = df02['clay'] / df02['total_p']
    df03['clay'] = df03['clay'] / df03['total_p']
    df04['clay'] = df04['clay'] / df04['total_p']
    df05['clay'] = df05['clay'] / df05['total_p']
    df06['clay'] = df06['clay'] / df06['total_p']

    #rename columns so we can combine into one dataframe with all horizons

    df01 = df01.rename(columns={'bulk_dens': "bulk_dens1", 'cec': 'cec1', 'clay': 'clay1', 'course_fra': 'course_fra1',
                                'silt': 'silt1', 'sand': 'sand1', 'ph': 'ph1', 'org_c_cont': 'org_c_cont1'
                                })

    df02 = df02.rename(columns={'bulk_dens': "bulk_dens2", 'cec': 'cec2', 'clay': 'clay2', 'course_fra': 'course_fra2',
                                'silt': 'silt2', 'sand': 'sand2', 'ph': 'ph2', 'org_c_cont': 'org_c_cont2'
                                })

    df03 = df03.rename(columns={'bulk_dens': "bulk_dens3", 'cec': 'cec3', 'clay': 'clay3', 'course_fra': 'course_fra3',
                                'silt': 'silt3', 'sand': 'sand3', 'ph': 'ph3', 'org_c_cont': 'org_c_cont3'
                                })

    df04 = df04.rename(columns={'bulk_dens': "bulk_dens4", 'cec': 'cec4', 'clay': 'clay4', 'course_fra': 'course_fra4',
                                'silt': 'silt4', 'sand': 'sand4', 'ph': 'ph4', 'org_c_cont': 'org_c_cont4'
                                })

    df05 = df05.rename(columns={'bulk_dens': "bulk_dens5", 'cec': 'cec5', 'clay': 'clay5', 'course_fra': 'course_fra5',
                                'silt': 'silt5', 'sand': 'sand5', 'ph': 'ph5', 'org_c_cont': 'org_c_cont5'
                                })

    df06 = df06.rename(columns={'bulk_dens': "bulk_dens6", 'cec': 'cec6', 'clay': 'clay6', 'course_fra': 'course_fra6',
                                'silt': 'silt6', 'sand': 'sand6', 'ph': 'ph6', 'org_c_cont': 'org_c_cont6'
                                })

    # merge all horizons into one dataframe
    df0 = pd.concat([df01, df02, df03, df04, df05, df06], axis=1)

    # calculate texture components over horizons by doing averages of profiles
    # e.g. sand content for 0-5cm horizon = avergae of sand content for profile 0cm and profile 5cm
    df0['sand_1'] = (df0['sand1'] + df0['sand2']) / 2
    df0['sand_2'] = (df0['sand2'] + df0['sand3']) / 2
    df0['sand_3'] = (df0['sand3'] + df0['sand4']) / 2
    df0['sand_4'] = (df0['sand4'] + df0['sand5']) / 2
    df0['sand_5'] = (df0['sand5'] + df0['sand6']) / 2
    df0['silt_1'] = (df0['silt1'] + df0['silt2']) / 2
    df0['silt_2'] = (df0['silt2'] + df0['silt3']) / 2
    df0['silt_3'] = (df0['silt3'] + df0['silt4']) / 2
    df0['silt_4'] = (df0['silt4'] + df0['silt5']) / 2
    df0['silt_5'] = (df0['silt5'] + df0['silt6']) / 2
    df0['clay_1'] = (df0['clay1'] + df0['clay2']) / 2
    df0['clay_2'] = (df0['clay2'] + df0['clay3']) / 2
    df0['clay_3'] = (df0['clay3'] + df0['clay4']) / 2
    df0['clay_4'] = (df0['clay4'] + df0['clay5']) / 2
    df0['clay_5'] = (df0['clay5'] + df0['clay6']) / 2
    df0['course_fra_1'] = (df0['course_fra1'] + df0['course_fra2']) / 2
    df0['course_fra_2'] = (df0['course_fra2'] + df0['course_fra3']) / 2
    df0['course_fra_3'] = (df0['course_fra3'] + df0['course_fra4']) / 2
    df0['course_fra_4'] = (df0['course_fra4'] + df0['course_fra5']) / 2
    df0['course_fra_5'] = (df0['course_fra5'] + df0['course_fra6']) / 2
    df0['ph_1'] = (df0['ph1'] + df0['ph2']) / 2
    df0['ph_2'] = (df0['ph2'] + df0['ph3']) / 2
    df0['ph_3'] = (df0['ph3'] + df0['ph4']) / 2
    df0['ph_4'] = (df0['ph4'] + df0['ph5']) / 2
    df0['ph_5'] = (df0['ph5'] + df0['ph6']) / 2
    df0['org_c_cont_1'] = (df0['org_c_cont1'] + df0['org_c_cont2']) / 2
    df0['org_c_cont_2'] = (df0['org_c_cont2'] + df0['org_c_cont3']) / 2
    df0['org_c_cont_3'] = (df0['org_c_cont3'] + df0['org_c_cont4']) / 2
    df0['org_c_cont_4'] = (df0['org_c_cont4'] + df0['org_c_cont5']) / 2
    df0['org_c_cont_5'] = (df0['org_c_cont5'] + df0['org_c_cont6']) / 2

    # drop old columns which are no longer useful
    df0 = df0.drop(['bulk_dens1', 'cec1', 'clay1',
                    'course_fra1', 'silt1', 'sand1', 'ph1', 'org_c_cont1',
                    'bulk_dens2', 'cec2', 'clay2', 'course_fra2', 'silt2',
                    'sand2', 'ph2', 'org_c_cont2', 'bulk_dens3', 'cec3',
                    'clay3', 'course_fra3', 'silt3', 'sand3', 'ph3', 'org_c_cont3',
                     'bulk_dens4', 'cec4', 'clay4', 'course_fra4', 'silt4',
                    'sand4', 'ph4', 'org_c_cont4', 'bulk_dens5', 'cec5', 'clay5',
                    'course_fra5', 'silt5', 'sand5', 'ph5', 'org_c_cont5',
                    'bulk_dens6', 'cec6', 'clay6', 'course_fra6', 'silt6', 'sand6', 'ph6',
                    'org_c_cont6'], axis=1)

    # apply functions
    df0["surface_texture"] = df0.apply(surf_texture, axis=1)
    df0["top_texture"] = df0.apply(top_texture, axis=1)

    # calculate awc value for each horizon
    df0["awc1"] = df0.apply(awc1, axis=1)
    df0["awc2"] = df0.apply(awc2, axis=1)
    df0["awc3"] = df0.apply(awc3, axis=1)
    df0["awc4"] = df0.apply(awc4, axis=1)
    df0["awc5"] = df0.apply(awc5, axis=1)
    # multiple awc value by depth
    # calculating AWC value by adding all of the horizons
    df0["awc_total"] = df0["awc1"] * 5 + df0['awc2'] * 10 + df0['awc3'] * 15 + df0['awc4'] * 30 + df0['awc5'] * 40

    # Conversions
    # convert ph values
    df0["ph_1"] = df0["ph_1"] / 10
    df0["ph_2"] = df0["ph_2"] / 10
    df0["ph_3"] = df0["ph_3"] / 10
    df0["ph_4"] = df0["ph_4"] / 10
    df0["ph_5"] = df0["ph_5"] / 10

    # calculate slope
    df0['slope'] = df0['gridcode'] / 10000

    # calculate LCC for subclasses
    df0["erosion_risk_LCC"] = df0.apply(erosion_risk_LCC, axis=1)
    df0["soil_tex_LCC"] = df0.apply(soil_tex_LCC, axis=1)
    df0["stoniness_LCC"] = df0.apply(stoniness_LCC, axis=1)
    df0["perm_LCC"] = df0.apply(perm_LCC, axis=1)
    df0["awc_LCC"] = df0.apply(LAWC_LCC, axis=1)
    df0["lime_LCC"] = df0.apply(lime_LCC, axis=1)

    df0["LCC_final"] = df0.apply(calc_LCC, axis=1)
    df0["LCC_final_noawc"] = df0.apply(calc_LCC_no_awc, axis=1)
    df0["limitation"] = df0.apply(limitation, axis=1)
    df0["limitation_noawc"] = df0.apply(limitation_noawc, axis=1)

    results_file = "LCC_SG_dosso_fullresults_" + str(i)

    df0.to_csv(results_file)

    print (str(i) + " completed!")








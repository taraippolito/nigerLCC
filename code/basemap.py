# SoilGrids LCC calculation algorithm
# to be run on 6 horizons : 0cm, 5cm, 15cm, 30cm, 60cm, 100cm
# run for each partition

# Import packages and dependencies
import numpy as np
import pandas as pd
import math
from simpledbf import Dbf5

#iterate over all 347 partitions of the dosso region
for i in range(347):
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





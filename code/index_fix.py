# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# index_fix.py
# Created on: 2020-01-22 13:57:53.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
dosso_index_10k_clip = "dosso_index_10k_clip"
dosso_index = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index"
index0_shp = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\index0.shp"

# Process: Feature Class to Feature Class
arcpy.FeatureClassToFeatureClass_conversion(dosso_index_10k_clip, dosso_index, "index0.shp", "\"FID\" =0", "", "")


# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# index_fish.py
# Created on: 2020-01-22 14:15:52.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
fish_125_0_shp = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\fish_125_0.shp"
fish_125_0_label_shp = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\fish_125_0_label.shp"

# Process: Create Fishnet
arcpy.CreateFishnet_management(fish_125_0_shp, "73125.5347290031 317001.005920411", "73125.5347290031 317011.005920411", "12.5", "12.5", "", "", "83125.534729005 327001.00592041", "NO_LABELS", "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\index0.shp", "POLYGON")


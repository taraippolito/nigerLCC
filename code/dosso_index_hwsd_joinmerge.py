# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# dosso_index_hwsd_joinmerge.py
# Created on: 2020-02-03 15:17:59.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
base0 = "base0"
HWSd_dosso_la_shp = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\HWSd_dosso_la.shp"
base_HWSD_0_shp = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_HWSD_0.shp"
HWSd_dosso_la = "HWSd_dosso_la"
base_HWSD_merge_0_shp = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_HWSD_merge_0.shp"

# Process: Spatial Join
arcpy.SpatialJoin_analysis(base0, HWSd_dosso_la_shp, base_HWSD_0_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "OBJECTID \"OBJECTID\" true true false 10 Long 0 10 ,First,#,C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\HWSd_dosso_la.shp,OBJECTID,-1,-1", "INTERSECT", "", "")

# Process: Merge
arcpy.Merge_management("C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_HWSD_0.shp;HWSd_dosso_la", base_HWSD_merge_0_shp, "OBJECTID \"OBJECTID\" true true false 10 Long 0 10 ,First,#,C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index\\base_HWSD_0.shp,OBJECTID,-1,-1,HWSd_dosso_la,OBJECTID,-1,-1")


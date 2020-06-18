# Import arcpy module
import arcpy
#path for finding files
path = "C:\\Users\\Research\\Documents\\Tara_Fall_2019\\dosso_index"
#base string for output files
outfile = path + "\\fish_125_net_"
#base string for input files
infile = path + "\\index"

#iterate over all the features
for i in range(347):
    outfile_index = outfile + str(i) + ".shp"
    infile_index = infile + str(i) + ".shp"
    for row in arcpy.da.SearchCursor(infile_index, ['SHAPE@', 'FID']):
        extent = row[0].extent
        left = extent.XMin
        bottom = extent.YMin
        right = extent.XMax
        top = extent.YMax
        bottom10 = bottom + 10

    arcpy.CreateFishnet_management(outfile_index, str(left) + " " + str( bottom), str(left) +" "+ str( bottom10), "12.5", "12.5", "", "", str(right) + " " + str( top), "NO_LABELS", infile_index, "POLYGON" )

import arcpy
mxd = arcpy.mapping.MapDocument(r"d:\data\Project.mxd")
df = arcpy.mapping.ListDataFrames(mdx, "New Data Frame")[0]


addlayer = arcpy.mapping.Layer(r"d:\data\Base_layers\commondata\areas_protegidas\Areas_protegidas.shp")
arcpy.mapping.AddLayer(df,addlayer,"BOTTOM")
addlayer = arcpy.mapping.Layer(r"D:\data\Base_layers\commondata\limite_nacional\bolivia-limites-nac.shp")
arcpy.mapping.AddLayer(df,addlayer,"BOTTOM")
addlayer = arcpy.mapping.Layer(r"D:\data\Base_layers\commondata\raster_data\Hansen_GFC2014_lossyear_10S_070W.TIF")
arcpy.mapping.AddLayer(df,addlayer,"BOTTOM")
addlayer = arcpy.mapping.Layer(r"D:\data\Base_layers\commondata\raster_data\Hansen_GFC2014_lossyear_00N_070W.TIF")
arcpy.mapping.AddLayer(df,addlayer,"BOTTOM")
addlayer = arcpy.mapping.Layer(r"D:\data\Base_layers\commondata\shps_bo_road\rvf_2010.shp")
arcpy.mapping.AddLayer(df,addlayer,"TOP")
symbologyLayer = "D:\data\hansen_style.lyr"
arcpy.ApplySymbologyFromLayer_management("Hansen_GFC2014_lossyear_00N_070W.tif",symbologyLayer)
arcpy.ApplySymbologyFromLayer_management("Hansen_GFC2014_lossyear_10s_070W.tif",symbologyLayer)
mxd.saveACopy(r"d:\data\project3.mxd")
	
'''
add the claslite file
calculate statistics on the claslite file
change the symbology of the claslite file
change the raster to a polygon

add the 653 bands of the landsat

list = [,,,"]
'''

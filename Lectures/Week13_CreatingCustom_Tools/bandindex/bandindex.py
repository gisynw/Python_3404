import arcpy
from arcpy.sa import *
from arcpy.sa import Raster
import os

red = Raster(arcpy.GetParameterAsText(0))
nir = Raster(arcpy.GetParameterAsText(1))
green = Raster(arcpy.GetParameterAsText(2))

index = arcpy.GetParameterAsText(3)
output_folder  = arcpy.GetParameterAsText(4)
output_name  = arcpy.GetParameterAsText(5)

## calculate index
if index == "NDVI":
    result = (nir - red)/ (nir + red)
else:
    result = (green - nir)/(green + nir)

# check folder exist
if not os.path.exists(output_folder):
    arcpy.AddError('The selected folder does not exist')
    raise arcpy.ExecuteError

# check file extension
if not output_name.lower().endswith(".tif"):
    output_name += ".tif"

# save file
output_path = os.path.join(output_folder, output_name)

result.save(output_path)

arcpy.AddMessage('Done')
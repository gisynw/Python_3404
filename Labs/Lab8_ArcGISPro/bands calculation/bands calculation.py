import arcpy
from arcpy.sa import *
from arcpy.sa import Raster
import os

arcpy.CheckOutExtension("Spatial")

# Input rasters (separate files)
red = Raster(arcpy.GetParameterAsText(0))
nir = Raster(arcpy.GetParameterAsText(1))
green = Raster(arcpy.GetParameterAsText(2))
swir1 = Raster(arcpy.GetParameterAsText(3))

# User choice of index
# index_type = arcpy.GetParameterAsText(4).upper()
index_type = arcpy.GetParameterAsText(4)
output_folder = arcpy.GetParameterAsText(5)
output_name = arcpy.GetParameterAsText(6)

# Calculate selected index
if index_type == "NDVI":
    result = (nir - red) / (nir + red)
elif index_type == "NDBI":
    result = (swir1 - nir) / (swir1 + nir)
elif index_type == "NDWI":
    result = (green - nir) / (green + nir)
else:
    arcpy.AddError("Invalid index type selected.")
    raise ValueError("Invalid index type")

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Ensure file extension is .tif
if not output_name.lower().endswith(".tif"):
    output_name += ".tif"

# Full output path
output_path = os.path.join(output_folder, output_name)

# Save and notify
result.save(output_path)

arcpy.AddMessage(f"{index_type} saved at: {output_path}")

import arcpy
from arcpy.sa import *
import numpy as np

# Parameters
input_shapefile = arcpy.GetParameterAsText(0)  # Input wildlife sightings point shapefile
output_polygons = arcpy.GetParameterAsText(1)  # Output shapefile for the hotspots
cell_size = arcpy.GetParameterAsText(2)  # Cell size
top_percentage = arcpy.GetParameterAsText(3)  # Top percentage for density threshold (e.g., 10 for top 10%)

# Check out the Spatial Analyst extension
# arcpy.CheckOutExtension("Spatial")

# Step 1: Calculate Point Density
density_raster = PointDensity(in_point_features = input_shapefile, population_field = None, cell_size=cell_size)
density_raster.save("in_memory/density_raster")

# Step 2: Calculate the Density Threshold Based on Input Percentage
# Convert the percentage to the corresponding percentile (e.g., 10% becomes the 90th percentile)
percentile_value = float(top_percentage)  # For top 10%, we need the 90th percentile
density_values = arcpy.RasterToNumPyArray(density_raster, nodata_to_value=-9999)
density_values = density_values[density_values > 0]  # Exclude no-data and zero density cells

if density_values.size == 0:
    arcpy.AddError("Density raster contains no valid values. Check your inputs or adjust cell size and search radius.")
    raise ValueError("Empty density raster array")
else:
    threshold_value = np.percentile(density_values, percentile_value)

# Step 3: Extract High-Density Areas Based on the Calculated Threshold
high_density_raster = Con(in_conditional_raster = density_raster < threshold_value, in_true_raster_or_constant = 1)

# Step 4: Convert High-Density Raster to Polygons
arcpy.RasterToPolygon_conversion(in_raster = high_density_raster, out_polygon_features = output_polygons, simplify = "NO_SIMPLIFY", raster_field = "VALUE")

# Cleanup
arcpy.Delete_management("in_memory/density_raster")
# arcpy.CheckInExtension("Spatial")

arcpy.AddMessage(f"Hotspot polygons created successfully using the top {top_percentage}% threshold (density threshold = {threshold_value}).")

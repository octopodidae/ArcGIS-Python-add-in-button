import arcpy
import pythonaddins
import uuid

class FeaturesToJSON(object):
    """Implementation for bla_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # Get the current map document and the first data frame.
        mxd = arcpy.mapping.MapDocument('current')
        #df = arcpy.mapping.ListDataFrames(mxd)[0]
        # Call the zoomToSelectedFeatures() method of the data frame class
        #df.zoomToSelectedFeatures()
        layers = arcpy.mapping.ListLayers(mxd)
        arcpy.FeaturesToJSON_conversion(layers[0], r"C:\bla\selection_" + str(uuid.uuid4()) + ".json")

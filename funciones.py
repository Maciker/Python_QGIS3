from qgis.core import *
from qgis.gui import *

@qgsfunction(args="auto", group="Custom", usesgeometry=True)
def hemisphere(geom, feature, parent):
	box = geom.boundingBox()
	if box.yMinimum() > 0 and box.yMaximum() > 0:
		return "N"
	if box.yMinimum() <= 0 and box.yMaximum() <= 0:
		return "S"
	else:
		return "B"
		
@qgsfunction(args="auto", group="Custom", usesgeometry=True)
def hemisphere_color(geom, feature, parent):
	box = geom.boundingBox()
	if box.yMinimum() > 0 and box.yMaximum() > 0:
		return 0
	if box.yMinimum() <= 0 and box.yMaximum() <= 0:
		return 255
	else:
		return 150

# Cuando se dispara la señal de nuevo proyecto, print hola:
iface.newProjectCreated.connect(lambda: print ("Hola"))
# Creamos la ventana de dialogo con el selector de crs
dialog = QgsProjectionSelectionDialog()
# Ejecutamos el dialogo
dialog.exec_()
# Vemos el crs elegido por el usuario:
dialog.crs()
<qgis._core.QgsCoordinateReferenceSystem object at 0x16903080>
dialog.crs().authid()
'EPSG:25830'
# Funcion que setea un crs
def setProjectCrs():
	dialog = QgsProjectionSelectionDialog()
	if dialog.exec_():
		crs = dialog.crs()
		QgsProject.instance().setCrs(crs)
# Nos conectamos a la señal y le pasamos la funcion
iface.newProjectCreated.connect(setProjectCrs)

#NO ejecutarlo como script si no añadir sentencias al editor.
# Creamos una capa en memoria
layer = QgsVectorLayer("Point?crs=EPSG:4326", "capa", "memory")
# Creamos el campo ID
field = QgsField("id", QVariant.String)
#Añadimos el campo a la capa
layer.dataProvider().addAttributes([field])
#Actualizamos la capa
layer.updateFields()
#Creamos un feature
feature = QgsFeature()
# Le pasamos los campos que tenemos en la capa
feature.setFields(layer.fields())
# Asignamos un valor al campo id, se puede hacer de diferentes maneras:
# con addAttributes pasando una lista
feature.addAttributes(["1"])
# con addAttribute pasando el numero del campo o su nombre y el valor:
feature.addAttribute(0, "2")
feature.addAttribute("id", "3")
#Creamos un punto
pt = QgsPointXY(1,1)
# Creamos la geometria desde el punto que hemos creado anteriormente
geom = QgsGeometry.fromPointXY(pt)
# Vemos la geometria
geom.asWkt()
# Le pasamos la geometria al feature
feature.setGeometry(geom)
#Añadimos el feature a la capa, desde el dataProvider
layer.dataProvider().addFeatures([feature])
# Ya podemos ver nuestro feature en el layer
list(layer.getFeatures())
# Ver sistema de coordenadas
layer.crs()
# Objeto tipo sistema de coordenadas <qgis._core.QgsCoordinateReferenceSystem object at 0x0C253A30>
layer.crs().authid()
'EPSG:4326'
# Crear sistemas de referencia
epsg4326 = QgsCoordinateReferenceSystem('EPSG:4326')
epsg3857 = QgsCoordinateReferenceSystem('EPSG:3857')
# Creamos unas transformacion entre geometrias
transformacion = QgsCoordinateTransform(epsg4326, epsg3857, QgsProject.instance())
# tenemos la geometria geom (1,1) y la vamoss a transformar:
geom
<QgsGeometry: Point (1 1)>
geom.asWkt()
'Point (1 1)'
# Ahora la transformamos de un sistema a otro:
geom.transform(transformacion)
0
geom.asWkt()
'Point (111319.49079327231447678 111325.14286638486373704)'

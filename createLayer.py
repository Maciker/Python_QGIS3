import random

def createLayer(n):
    layer = QgsVectorLayer("Point?crs=EPSG:4326", "capa", "memory")
    layer.dataProvider().addAttributes([QgsField("id", QVariant.Int)])
    layer.updateFields()
    features =[]
    for i in range(n):
        feature = QgsFeature()
        feature.setFields(layer.fields())
        feature.setAttributes([i])
        x = random.uniform(-100,100)
        y = random.uniform(-50,50)
        pt = QgsPointXY(x,y)
        geom = QgsGeometry.fromPointXY(pt)
        feature.setGeometry(geom)
        features.append(feature)
    layer.dataProvider().addFeatures(features)
    return layer
    
randomlayer = createLayer(50)
print (len(list(randomlayer.getFeatures())))
QgsProject.instance().addMapLayer(randomlayer)
        
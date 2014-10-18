<<<<<<< HEAD
# This program will show the number of streams and spring  at a user specified distance 
=======
# This show the number of streams and spring  at a user specified distance a
>>>>>>> origin/master
# from on oil and/or gas well Within any user specified county in the state of 
# Utah. 
# Data was obtained from the Utah's Automated Geographic Reference Center (AGRC) 
# http://gis.utah.gov/data/

# It will be GIS User specific
# It will use arcpy.mapping
# It will manipulate or show relationship to another data source
# It will have a log detailing the process
# It will be interactive with the user somehow


# Data was obtained from the Utah's Automated Geographic Reference Center (AGRC) 
# http://gis.utah.gov/data/
# Program completed on 10/06/2014
# By Jeremy Jackson

import os
import arcpy
import time

# path variables

myDataPath = " C:\\  " # enter a path were your data is stored
myOutPutPath = "C:\\ " # enter a path were your results/GeoDataBase will be stored

# data Variables
county_Layer = myDataPath + "\\" + "Counties" + "\\" + "Counties.shp"
OilGasWells_Layer = myDataPath + "\\" + "DNROilGasWells" + "\\" + "DNROilGasWells.shp"
Lakes_Layer = myDataPath + "\\" + "LakesNHDHighRes" + "\\" + "LakesNHDHighRes.shp" 
Rivers_Layer = myDataPath + "\\" + "UtahMajorRiversPoly" + "\\" + "UtahMajorRiversPoly.shp"
springs_Layer = myDataPath + "\\" + "SpringsNHDHighRes" + "\\" + "SpringsNHDHighRes.shp"
streams_Layer =  myDataPath + "\\" + "StreamsNHDHighRes" + "\\" + "StreamsNHDHighRes.shp"
Roads_Layer =  myDataPath + "\\" + "UDOTRoutes_LRS" + "\\" + "UDOTRoutes_LRS.shp"
Cities_layer = myDataPath + "\\" + "Municipalities" + "\\" + "Municipalities.shp"

startTime = time.asctime()

# county abbreviation dictionary


UtahCounties = { "beaver":"BEAVER",
                "box elder":"BOX ELDER",
                "cache" :  "CACHE",
                "carbon" : "CARBON" ,
                "daggett" : "DAGGETT",
                "davis" : "DAVIS",
                "duchesne" : "DUCHESNE",
                "emery" : "EMERY",
                "garfield" : "GARFIELD",
                "grand" : "GRAND",
                "iron" : "IRON" ,
                "juab": "JUAB",
                "kane": "KANE",
                "millard" : "MILLARD",
                "morgan": "MORGAN",
                "piute": "PIUTE",
                "rich" : "RICH",
                "salt lake" : "SALT LAKE",
                "san juan" : "SAN JUAN",
                "sanpete" : "SANPETE",
                "sevier" : "SEVIER",
                "summit" : "SUMMIT" ,
                "tooele" : "TOOELE",
                "uintah" : "UINTAH",
                "utah" : "UTAH" ,
                "wasatch" : "WASATCH",
                "washington" : "WASHINGTON" ,
                "wayne" : "WAYNE" ,
                "weber" : "WEBER" ,
                
                }

CountyName = raw_input("Enter the name of a county in Utah. >").lower()

while CountyName not in UtahCounties:
                                    CountyName = raw_input("Enter the name of a county in Utah. >").lower()


CountyName = UtahCounties[CountyName]



# create directory
project_name = raw_input("Enter the Name for your project :>")
project_dir = myOutPutPath + "\\" + project_name




while os.path.isdir(project_dir) == True:
    project_name = raw_input("project exists enter a new project name :>")
    project_dir = project_dir= myOutPutPath + "\\" + project_name

Buffer = raw_input("Please enter the distance around oil well in Meters :> ")

os.makedirs(project_dir)
DirTime = time.asctime()
print "Directory %s created  @ \t %s " % (project_name,DirTime)



# create GDB

arcpy.CreateFileGDB_management(project_dir,project_name, "CURRENT")
projectGDB = project_dir + "\\" + project_name + ".gdb"
GDBTime = time.asctime()
print "Geodatabase %s created @ \t %s " % (project_name,GDBTime)

#------------------------- WorkSpace Preperation -------------------------------
# copy template
template = arcpy.mapping.MapDocument(myOutPutPath + "\\" + "template.mxd")
projectMXD = project_dir + "\\" + project_name + "map.mxd"

template.saveACopy(projectMXD)

del template
TempTime = time.asctime()
print "Template Copied @  \t \t %s " % (TempTime)

# define map elements
mxd = arcpy.mapping.MapDocument(projectMXD)
df = arcpy.mapping.ListDataFrames(mxd)[0]

# add queryable layers to mxd

countyLayer = arcpy.mapping.Layer(county_Layer)


county = arcpy.mapping.AddLayer(df,countyLayer,"TOP")


queryLayers = arcpy.mapping.ListLayers(mxd, "", df)
QueryLayerTime = time.asctime()

print "Query Layers added to map @ \t %s " % (QueryLayerTime)

 
queryLayers[0].definitionQuery = '"NAME"' + "=" + "'" + CountyName + "'"

# zoom to selected layer

arcpy.SelectLayerByAttribute_management(queryLayers[0],"NEW_SELECTION",'"NAME"' + "=" + "'" + CountyName + "'")
df.zoomToSelectedFeatures()

# Clip state wide data to user specified county


countyClip = project_dir + "\\" + CountyName + "countyClip.lyr"
queryLayers[0].saveACopy(countyClip)



arcpy.Clip_analysis(springs_Layer ,countyClip,projectGDB + "\\springs", "")
arcpy.Clip_analysis(OilGasWells_Layer,countyClip,projectGDB + "\\OilGasWells", "")
arcpy.Clip_analysis(Lakes_Layer ,countyClip,projectGDB + "\\Lakes", "")
arcpy.Clip_analysis(Rivers_Layer ,countyClip,projectGDB + "\\Rivers", "")
arcpy.Clip_analysis(streams_Layer  ,countyClip,projectGDB + "\\Streams", "")
arcpy.Clip_analysis(Roads_Layer ,countyClip,projectGDB + "\\Roads", "")
arcpy.Clip_analysis(Cities_layer ,countyClip,projectGDB + "\\Cities", "")

CountyClipTime = time.asctime()
print "Clipped %s County Data to map  @ \t %s " % (CountyName,CountyClipTime)

# add Clipped data to map


springsLayer = arcpy.mapping.Layer(projectGDB + "\\springs")
OilGasWellsLayer= arcpy.mapping.Layer(projectGDB + "\\OilGasWells")
LakesLayer = arcpy.mapping.Layer(projectGDB + "\\Lakes") 
RiversLayer = arcpy.mapping.Layer(projectGDB + "\\Rivers")
StreamsLayer = arcpy.mapping.Layer(projectGDB + "\\Streams")
RoadsLayer = arcpy.mapping.Layer(projectGDB + "\\Roads")
CitiesLayer = arcpy.mapping.Layer(projectGDB + "\\Cities")

# ----------------------------GEOPROCESSING -------------------------------------------
# Creating a buffer around Oilwells at user specified distance

OilGasWellsBuffer = projectGDB + "\\OilGasWellsBuffer"
StreamsBufferClip = projectGDB + "\\StreamsBufferClip"
SpringsBufferCLip = projectGDB + "\\SpringsBufferCLip"
bufferTime = time.asctime()

print "Buffer started @ \t %s " % (bufferTime)
# Process: Buffer
arcpy.Buffer_analysis(OilGasWellsLayer, OilGasWellsBuffer, Buffer + " " + "Meters", "FULL", "ROUND", "ALL", "")
bufferFTime = time.asctime()
print "Buffer Finished @ \t %s " % (bufferFTime)
# Process: Clipping streams to oilwellsbuffer
StreamClip = time.asctime()
print "started clipping data  @ \t %s " % (StreamClip) 

arcpy.Clip_analysis(StreamsLayer, OilGasWellsBuffer, StreamsBufferClip, "")

# Process: Clipping springs to oil wells buffer

StreamFClip = time.asctime()
print "Finished clipping data  @ \t %s " % (StreamFClip) 
arcpy.Clip_analysis(springsLayer, OilGasWellsBuffer, SpringsBufferCLip, "")

StreamsBufferClipLayer = arcpy.mapping.Layer(projectGDB + "\\StreamsBufferClip")
SpringsBufferClipLayer = arcpy.mapping.Layer(projectGDB + "\\SpringsBufferClip")

#-------------------Final Map Creation----------------------------------------------------------
print "adding data to map"
Cities = arcpy.mapping.AddLayer(df,CitiesLayer,"TOP")
 
Lakes = arcpy.mapping.AddLayer(df,LakesLayer,"TOP") 
Rivers = arcpy.mapping.AddLayer(df,RiversLayer,"TOP")

Roads = arcpy.mapping.AddLayer(df,RoadsLayer,"TOP")

SpringNearOilwell = arcpy.mapping.AddLayer(df,SpringsBufferClipLayer,"TOP")
StreamsNearOilwell = arcpy.mapping.AddLayer(df,StreamsBufferClipLayer,"TOP")




endtime = time.asctime()

print " Finished creating map @ \t %s " % (endtime)
# Create Log File
log = open(project_dir + "\\" + project_name + "_log.txt", "a")
log.write("project started " +"\t" + startTime + "\n"
          "Directory   %s created         @ \t %s " % (project_name,DirTime) + "\n" +
          "Geodatabase %s created         @ \t %s " % (project_name,GDBTime) + "\n" +
          "Template Copied                @ \t %s " % (TempTime) + "\n" +
          "Query Layers added             @ \t %s " % (QueryLayerTime) + "\n" +
          "Clipped %s County Data to map  @ \t %s " % (CountyName,CountyClipTime) + "\n" +
          "Buffer started                 @ \t %s " % (bufferTime) + "\n" +
          "started clipping data          @ \t %s " % (StreamClip) + "\n" +
          "Finished clipping data         @ \t %s " % (StreamFClip) + "\n" +
          "Finished creating map          @ \t %s " % (endtime))
log.close()

print " Log file created"
#open map in ArcMap. 
 
os.system("start " + projectMXD)


# Clean up workspace
mxd.save()
del mxd
print "Done"



                         






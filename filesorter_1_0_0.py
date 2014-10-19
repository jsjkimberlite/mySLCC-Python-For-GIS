# This is a python program I wrote to sort files and store their paths
# by Jeremy Jackson
# version 1.0.0

import os

print "started"

# path varibles


dataPath =  "A path on your comp"
dataInputPath = dataPath + "\\Data Folder"

print dataPath
print dataInputPath

FileList = os.listdir(dataInputPath)

print FileList

TextFilePath = [] 
TextFileList = [] 
numTextFiles = 0
DocFilePath  = [] 
DocFileList  = [] 
numDocFiles  = 0
xlsFilePath  = [] 
xlsFileList  = [] 
numxlsFiles  = 0
pptFilePath  = [] 
pptFileList  = [] 
numpptFiles  = 0
j = -1

for i in FileList:
    
    j = j + 1
    if i[-4:] == ".txt":
        print i + " is a txt file."
        TextFileList.append(FileList[j])
        TextFilePath.append(dataInputPath + "\\" + TextFileList[numTextFiles])
        numTextFiles = numTextFiles + 1
    
    if i[-4:] == ".doc":
        print i + " is a doc file."
        DocFileList.append(FileList[j])
        DocFilePath.append(dataInputPath + "\\" + DocFileList[numDocFiles])
        numDocFiles = numDocFiles + 1
        
    if i[-4:] == ".xls":
        print i + " is a xls file."
        xlsFileList.append(FileList[j])
        xlsFilePath.append(dataInputPath + "\\" + xlsFileList[numxlsFiles])
        numxlsFiles = numxlsFiles + 1
        
    if i[-4:] == ".ppt":
        print i + " is a ppt file."
        pptFileList.append(FileList[j])
        pptFilePath.append(dataInputPath + "\\" + pptFileList[numpptFiles])
        numpptFiles = numpptFiles + 1
print numTextFiles
print numDocFiles
print numxlsFiles
print numpptFiles

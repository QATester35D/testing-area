import requests
import json
import time

class GetEarthquakeInfo:
    def __init__(self,startDate, endDate):
        #Looks like: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02
        earthquakeDayData='https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime='+startDate+'&endtime='+endDate
        self.usgsEarthquakeApi=requests.get(earthquakeDayData)

    def getEarthquakeData(self):
        r=self.usgsEarthquakeApi
        if r.status_code != 200:
            print ("Problem connecting with USGS Earthquake API at https://earthquake.usgs.gov/earthquakes.")
            exit
        # self.delete_file_if_exists(fname) #delete the file if it already exists so we don't append to it
        # f = open(fname, "a")
        earthquakeList = []
        theJSON = json.loads(r.content)
        # timeframeCountOfEarthquakes=i["count"] #do I want this value?
        propertyList=["mag", "place", "felt", "tsunami", "sig", "type", "title"]
        propListLen=len(propertyList) #7
        for i in theJSON["features"]:
            rowCtr=1
            # propListColCtr=0
            for aRow in i["properties"]: #aRow is the actual property name
                for aCol in range(propListLen):
                    tempProp=propertyList[aCol]
                    tempVal=i["properties"][tempProp]
                    if aRow == tempProp:
                        # earthquakeList.append[rowCtr, aCol] = tempVal
                        earthquakeList.append((rowCtr,aCol))=tempVal
                        # earthquakeList[rowCtr, aCol] = ["place"]
                        # earthquakeList[rowCtr, aCol] = ["felt"]
                        # earthquakeList[rowCtr, aCol] = ["tsunami"]
                        # earthquakeList[rowCtr, aCol] = ["sig"]
                        # earthquakeList[rowCtr, aCol] = ["type"]
                        # earthquakeList[rowCtr, aCol] = ["title"]
            rowCtr+=1
                # propListColCtr+=1
        return earthquakeList

#Calling a class to parse thru the API json and creates a text file of the info for the schedule
startDate='2024-06-01'
endDate='2024-06-02'
a=GetEarthquakeInfo(startDate, endDate)
eqData=a.getEarthquakeData()
time.sleep(1)

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
        earthquakeList = []
        theJSON = json.loads(r.content)
        reportCount=theJSON["metadata"]["count"] #using this as the row count
        propertyList=["mag", "place", "felt", "tsunami", "sig", "type", "title"] #A list of the properties I want
        propListLen=len(propertyList) #7
        for rowCtr in range (reportCount):
            for i in theJSON["features"]:
                propertyListCtr=0
                row = []
                for aRow in i["properties"]: #aRow is the actual property name
                    tempProp=propertyList[propertyListCtr]
                    tempVal=i["properties"][tempProp]
                    if aRow == tempProp:
                        row.append(tempVal)
                        propertyListCtr+=1
                earthquakeList.append(row) #appending the entire row of data once to the list
        return earthquakeList

#Calling a class to parse thru the API json and creates a text file of the info for the schedule
startDate='2024-06-01'
endDate='2024-06-02'
a=GetEarthquakeInfo(startDate, endDate)
eqData=a.getEarthquakeData()
time.sleep(1)

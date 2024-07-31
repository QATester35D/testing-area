import requests
import json
import os
import sys
from openpyxl import Workbook

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
        earthquakeDictionary = {}
        theJSON = json.loads(r.content)
        for i in theJSON["Feature"]:
            dateGameOfWeek = i["mag"] #"brand": "Ford",
            dayAbbrev = i["place"]
            dayNumberOfGames = i["felt"]
            dayNumberOfGames = i["tsunami"]
            dayNumberOfGames = i["sig"]
            dayNumberOfGames = i["type"]
            dayNumberOfGames = i["title"]
            for aRow in i["games"]:
                awayTeamName = aRow["awayTeam"]["placeName"]["default"]
                awayTeamAbbrev = aRow["awayTeam"]["abbrev"]
                homeTeamName = aRow["homeTeam"]["placeName"]["default"]
                homeTeamAbbrev = aRow["homeTeam"]["abbrev"]
                gameInfo=dateGameOfWeek+","+dayAbbrev+","+str(dayNumberOfGames)+","+awayTeamAbbrev+","+homeTeamAbbrev+'\n'
        #         f.write(gameInfo)
        # f.close()

#Calling a class to parse thru the API json and creates a text file of the info for the schedule
startDate='2024-07-29'
endDate='2024-07-29'
a=GetEarthquakeInfo(startDate, endDate)
a.getEarthquakeData()


#######################################################################################################
# This is a scratch area for figuring things out.
#######################################################################################################
import time
import datetime
import math
import re
##############################################################
import urllib.request, urllib.parse, urllib.error
import json
##############################################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)

print(person) 

time.sleep(1)

##############################################################
earthquakeURL =  "http://earthquake.usgs.gov/fdsnws/event/1/query?"
paramD = dict()
paramD["format"] = "geojson"                 # the format the data will be in
paramD["starttime"] = "2019-06-01T00:00:00"  # the minimum date/time that might be retrieved
paramD["endtime"] = "2019-06-30T23:59:59"    # the maximum date/time that might be retrieved
paramD["minmag"] = 6                         # the smallest earthquake magnitude to return
paramD["limit"] = 5                          # the maximum number of earthquakes to return
                                             # starts with the most recent
#Builds this: Retrieving http://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-06-01T00%3A00%3A00&endtime=2019-06-30T23%3A59%3A59&minmag=6&limit=5
params = urllib.parse.urlencode(paramD)
print('Retrieving', earthquakeURL+params)
uh = urllib.request.urlopen(earthquakeURL+params)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
        
if not js or 'type' not in js :
    print('==== Failure To Retrieve ====')
    print(data)
    
# Output first Record
print("\nFirst Earthquake")
lng = js["features"][0]["geometry"]["coordinates"][0] # retrieve the first item in features array
lat = js["features"][0]["geometry"]["coordinates"][1] # look in "geometry" object
dep = js["features"][0]["geometry"]["coordinates"][2] # get the first, second, and third coordinates
print('lng', lng, 'lat', lat, 'depth', dep)

# retrieve the first item in features array, look in the properties object, return the place object
location = js["features"][0]["properties"]["place"]
print(location, "\n")

# Loop through entire data set
print("\nAll Earthquakes")
count = 0
for f in js["features"]:
    lng = f["geometry"]["coordinates"][0]
    lat = f["geometry"]["coordinates"][1]
    dep = f["geometry"]["coordinates"][2]
    print('lng', lng, 'lat', lat, 'depth', dep)
    location = f["properties"]["place"]
    print(location, "\n")
    count = count+1
print(count)




###############################################################
# Initialize an empty 2D list
two_d_list = []

# Dynamically add rows and columns
for i in range(3):  # For example, add 3 rows
    row = []
    for j in range(4):  # For example, add 4 columns to each row
        row.append(i * j)  # Populate with some values, e.g., the product of indices
    two_d_list.append(row)

# Print the dynamically created 2D list
for row in two_d_list:
    print(row)

time.sleep(1)
#########
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

time.sleep(1)
#################################################################################
# x=1
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
# else:
#   print("Nothing went wrong")

# time.sleep(1)

# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

try:
  f = open("c:\\temp\\demofile.txt","w")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

time.sleep(1)

#################################################################################
# Power operator
#################################################################################
# Power operator: number ** exponent
# pow() function
square = pow(5, 2)
print(square)
# 25

# The pow() function also receives a third argument: the modulo. The sign for modulo is %. This argument evaluates the remainder when a value is divided by another.
#   For example, 5 % 2 gives 1 because 5 divided by 2 is 2, remainder 1.
# Applying the modulo the pow() function looks like this:

mod = pow(5, 2, 3)
print(mod)
## 1
## 5 * 5 is 25
## 25 % 3 is 1


# math.pow() comes from Python's math module. This function is similar to the in-built pow() function
# in usage and syntax, except that it has two differences:
# - it only accepts two arguments: the base and the exponent
# - it always returns a float number even when the raised number is a whole number.
# - So, math.pow(5, 2) returns 25.0.
print(math.pow(5, 2))

#################################################################################
# Date stuff
#################################################################################

x = datetime.datetime(2024, 5, 17, 17, 30, 5)
print(x)

# x = datetime.datetime.now()
# print(x.year) #prints the year only
# print(x.strftime("%A")) #prints the day of the week

time.sleep(1)
#################################################################################
# Messing with scope
#################################################################################
x="John"
def myfunc1(x):
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  print(x)
  return x

print(myfunc1(x))
print(x)

time.sleep(1)
#################################################################################
# Iterators
#################################################################################

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print("\n")
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("ham", "bacon", "sausage")
for x in mytuple:
  print(x)

mystr = "holiday"
for x in mystr:
  print(x)

time.sleep(1)

#################################################################################
bubbleArrayList=[2,12,4,15,3]
print("The starting list is: ",bubbleArrayList)
listCounter=0
looping = 0
lengthOfList=len(bubbleArrayList)
for i in range(lengthOfList-1):
    swapped=False
    for j in range(lengthOfList-i-1):
        currentVal=bubbleArrayList[j]
        nextValue=bubbleArrayList[j+1]
        if (currentVal > nextValue):
            bubbleArrayList[j]=nextValue
            bubbleArrayList[j+1]=currentVal
            swapped=True
    if not swapped:
        break
print("The sorted list is now: ",bubbleArrayList)
time.sleep(1)
#################################################################################
#STDIN and STDOUT 
n = int(input("Enter in a number: "))        # Reading input from STDIN
s = input("Enter in a string: ")             # Reading input from STDIN
n=n*2
print(n)                # Writing output to STDOUT
print(s)                # Writing output to STDOUT
time.sleep(1)
#################################################################################
# Removing spaces from a string using replace method
#################################################################################
wordToRemoveSpaces=" The string with spaces "
print("The string being used to strip spaces out of is:",wordToRemoveSpaces)
newWord=wordToRemoveSpaces.replace(" ","")
print (f"The string has no spaces now and is one big word, it is: {newWord}.")
time.sleep(1)

#######################################################################################################
# Largest subarray with equal number of 0s and 1s - gets the starting and ending indexes of the largest 
# subarray with equal number of 0s and 1s. Also returns the size of such subarray.
def findLargestSubArray(arr, n):
    sum = 0
    maxsize = -1

    # Pick a starting point as i
    for i in range(0, n-1):
        sum = -1 if(arr[i] == 0) else 1

        # Consider all subarrays starting from i
        for j in range(i + 1, n):
            sum = sum + (-1) if (arr[j] == 0) else sum + 1
            # If this is a 0 sum subarray, then compare it with maximum size subarray calculated so far
            if (sum == 0 and maxsize < j-i + 1):
                maxsize = j - i + 1
                startindex = i

    if (maxsize == -1):
        print("No such subarray");
    else:
        print(startindex, "to", startindex + maxsize-1);

    return maxsize

# arr = [1, 0, 0, 1, 0, 1, 1] #sub-array 0, 0, 0, 1, 1, 1 <=> 0 to 5
arr = [1, 0, 0, 1, 0, 1, 1, 0] #sub-array 0, 0, 0, 0, 1, 1, 1, 1 <=> 0 to 7
arraySize = len(arr)
findLargestSubArray(arr, arraySize)
print("wait")

##################################
#Find the mininum value in a List
##################################
my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:',minVal)
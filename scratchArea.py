#######################################################################################################
# This is a scratch area to work through various concepts.
# If a common concept is coded, then it is moved to a separate file if deemed worth separating.
#######################################################################################################
import time

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
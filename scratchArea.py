#######################################################################################################
# Working through various concepts
#######################################################################################################
import time

# Removing spaces from a string using replace method
wordToRemoveSpaces=" The string with spaces "
print("The string being used to strip spaces out of is:",wordToRemoveSpaces)
newWord=wordToRemoveSpaces.replace(" ","")
print (f"The string has no spaces now and is one big word, it is: {newWord}.")
time.sleep(1)

# Largest subarray of 0's and 1's - gets the starting and ending indexes of the largest 
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
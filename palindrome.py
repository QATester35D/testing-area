#################################################################
# Multiple ways to check if a word is a palindrome
###############################################################################################
# Version 1 - strip out space and compare first and last, working inward
# Note that if a space has to be stripped out, then it is two words and not truly a Palindrome
###############################################################################################
def isThisAPalindrome(teststr):  
    lowerCaseWord=str.lower(teststr)
    newLowerCaseWord=''.join(filter(str.isalnum, lowerCaseWord))
    wordLength=len(newLowerCaseWord)-1
    firstLoopIteration=True
    for i in newLowerCaseWord:
        firstChar=i
        if firstLoopIteration == True:
            firstLoopIteration = False
            endNum=wordLength
        else:
            endNum=endNum - 1
        lastChar=newLowerCaseWord[endNum]
        if firstChar != lastChar:
            print (teststr," is not a palindrome. we're done.")
            return False
    print("The word ",teststr," is a palindrome.")
    return True

test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.","Race car!"]
for word in test_words:
    print(isThisAPalindrome(word))

############################################################################################
# Version 2 - using the reverse approach and work backwards using the string[index] operator
############################################################################################
def isPalindrome(string): 
    if (string == string[::-1]):
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 
 
#Enter input string 
string = input ("Is this a Palindrome? Using the reverse string index operator - Enter a string: ")
print(isPalindrome(string))

#################################################################
# Version 3 - using the reversed and join methods
#################################################################
def isPalindrome(string):
    revstr=''.join(reversed(string))
    if string==revstr:
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."
 
#Enter input string
string = input ("Is this a Palindrome? Using the \"reversed\" method - Enter a string: ")
print(isPalindrome(string))

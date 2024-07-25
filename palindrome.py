def is_palindrome(teststr):  
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

#palindrome
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.","Race car!"]
for word in test_words:
    print(is_palindrome(word))

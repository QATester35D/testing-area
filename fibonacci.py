#################################################################################
# Creating a basic Fibonnaci where you add the previous number to the next number
# Because it calls itself, you can't pass in the loop range
#################################################################################
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 10:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

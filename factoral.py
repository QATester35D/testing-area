def factorial(n):

    if n < 0: 

        return "Invalid input, negative number" 

    elif n == 0: 

        return int(1)

    else:

        fact = 1 

        # for i in range(1, n+1): 
        for i in range(1, n+1):

            fact *= i 

        return fact 

print(factorial(5))

print(factorial(-3)) 

print(factorial(0)) 
# Function to check if a number is prime 

def is_prime(n): 
    if n <= 1: 
        return False 

    for i in range(2, n): 
        if n % i == 0: 
            return False 

    return True 


primes = [] 

for i in range(2, 20): 
    if is_prime(i):
        primes.append(i) 

print("Prime numbers:", primes) 
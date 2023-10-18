import math

def largest_prime_factor(n):
    #Start with the smallest prime factor: 2
    factor = 2

    #Keep dividing the number by the smallest prime factor until it is no longer divisible
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            #Increment the factor if it is not a divisor
            factor += 1

    #If the remaining number is greater than 1, it is the largest prime factor
    if n > 1: 
        return n 
    else:
        #If the number itself is a prime number, return the number itself
        return factor

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
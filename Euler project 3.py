import time


start_time = time.time()  # Record the start time

def Isprime (n):
    for i in range (2,int(n**0.5)):
        if n%i==0:
            return False
    return True

number = 6008514751411133
for i in range (1,int(number**0.5)):
    if number%i ==0:
        if (Isprime(i))== True:
            print (i)

# import time

# def Isprime(n):
#     if n < 2:  # Handle edge cases
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# number = 60085147514003

# start_time = time.time()  # Record the start time

# largest_prime = 1

# # Start from the largest potential factor and work down
# for i in range(int(number**0.5), 1, -1):
#     if number % i == 0:  # Check if i is a factor
#         if Isprime(i):  # Check if the factor is prime
#             largest_prime = i
#             break  # Stop as soon as we find the largest prime factor

# end_time = time.time()  # Record the end time

            
end_time = time.time()  # Record the end time
print("Execution Time: {:.5f} seconds".format(end_time - start_time))

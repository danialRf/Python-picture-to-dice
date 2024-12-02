import time

start_time = time.time()


def IsPrime(n):
    if n<=2:
        return False
    for i in range (2,int(n**0.5)+1):
        if (n%i)==0:
            return False
    return True
num = 0

# print (IsPrime(23))

for i in range (0,10000000):
    if IsPrime(i)==True:
        print(i)

 
end_time = time.time()

program_time = end_time - start_time
print(f"Execution time: {program_time} seconds")

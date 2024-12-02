def Iseven (n):
    return n%2==0
FirstNumber=1
SecondNumbher=2
sum=0
while (FirstNumber<4000000):
   New = SecondNumbher+FirstNumber
   FirstNumber=SecondNumbher
   SecondNumbher=New
   if (Iseven(FirstNumber)):
       sum+=FirstNumber

print(sum)
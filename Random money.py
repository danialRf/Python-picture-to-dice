import random
import matplotlib.pyplot as plt

random.seed()

people=[]
for i in range (0,50):
    people.append(100)

for i in range (1,1000000):
    for person in range (0,50):
        person2=random.randrange(0,50)
        while people[person2]==0:
            person2 = random.randrange(0,50)
        if people[person]!=0:
            #print (person,person2)
            people[person]=people[person]-1
            people[person2]=people[person2]+1

people.sort()
plt.bar(range(0,50),people)
plt.show()
print (people)
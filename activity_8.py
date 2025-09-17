#Print 1 to 20
count1 = [value for value in range(1,21)]
print(f"count 1 to 20:{count1}\n")

#Print 1 to 1,000,000
#for value in range(1,1000001):
#    print(value)

#Get the minimum, maximum and sum of 1 to 1,000,000
oneMillion = range(1,1000001)
print(f"minimum:{min(oneMillion)}")
print(f"maximum:{max(oneMillion)}")
print(f"sum:{sum(oneMillion)}\n")

#Odd numbers
oddNumbers = [value for value in range(1, 20, 2)]
print(f"odds:{oddNumbers}\n")

#List multiple by 3, from 3 to 30
for value in range(3,31,3):
    print(f"multiply by 3:{value}\n")

#Cube of 1 to 10
cube = [value**3 for value in range(1,11)]
print(f"cube:{cube}\n")

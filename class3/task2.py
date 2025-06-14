Values = []
sum = 0

while sum < 100:
    num = int(input("Enter an integer: "))
    Values.append(num)      #store in Values
    sum += num            #add to sum

print("Condition was met. The sum is ", sum)
print("Values: ", Values)

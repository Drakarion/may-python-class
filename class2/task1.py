age=int(input("How old are you: "))

if age>0 and age<13:
    print(f"You are child")
elif age >=13 and age<18:
    print(f"You are teenager")
elif age >=18 and age<65:
    print(f"You are adult")
elif age>=65:
    print(f"You are elder")
else:
    print("Provide right age")
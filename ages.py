name = input("Enter your name:")
print("Enter your age:")
age = int(input())

if age < 12:
    print(name + " is Child")
elif age >= 12 and age <= 18:
    print(name +" is Teenager")
else:
    print(name +" is Adult")
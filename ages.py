#Task 1

name = input("Enter your name:")
print("Enter your age:")
age = int(input())


def ages(name: str, age:int )->str:
    if name.isdigit():
        raise TypeError("Invalid type for name ")

    if not isinstance(age , int):
       raise TypeError("Invalid type for age")

    if age < 12:
        return "child"
    elif age >= 12 and age <= 18:
        return "teenager"
    else:
        return "adult"


result = ages(name, age)

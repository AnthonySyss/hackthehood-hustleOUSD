check = "yes"
ages = [15, 22, 18, -7, 30, 12, 3, 19, -5]
age = ages[0]
i = 0

while check =="yes" and ages:
    age = ages.pop(0)

    if age < 0:
        print(f"{age}, Invalid age, negative ages are not allowed.")
    elif age < 18:
        print(f"{age}, Under 18, not allowed to vote.")
    else:
        print(f"{age}, Eligible to vote.")

    if ages:
        check = input("Do you want to check another age? (yes/no): ")
    else:
        print("No more ages to check.")
        break
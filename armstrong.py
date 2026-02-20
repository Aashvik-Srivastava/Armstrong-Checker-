def is_armstrong (num):
    n = len(str(num))
    sum_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** n
        temp //= 10
    return sum_digits == num 

while True:

    print("\nArmstong Number checker")
    print("1. Check a single number ")
    print("2. Show All Armstong number in a range")
    print("3. Exit")


    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        num = int(input("Enter a number to check: "))
        if is_armstrong(num):
            print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is not an Armstrong number ")
            



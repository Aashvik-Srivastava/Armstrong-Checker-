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
    

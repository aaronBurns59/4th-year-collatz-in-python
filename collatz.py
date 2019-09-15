# a python program which carries out the collatz conjecture

n = 20

# keep going until n is equal to 1
while n != 1:
    print(n)
    # if the number is even
    if n % 2 == 0:
        # if the number is even divide it by 2
        n /= 2
    else: 
        # if the number is even multiple it by 3
        n = (n * 3) + 1

print(n)

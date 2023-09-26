number = int(input("Number: "))
factor = 1
total = 0

for i in range(number):
    if number%factor == 0:
        total += 1
        factor += 1
    else:
        factor += 1

print(total)
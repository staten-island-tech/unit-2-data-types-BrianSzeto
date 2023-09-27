num = int(input("Number: "))
list = []



for i in range(1, num + 1):
    if num % i == 0:
        list.extend([i])

print(list)
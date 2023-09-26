num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
list1 = []
list2 = []



for i in range(1, num1 + 1):
    if num1 % i == 0:
        list1.extend([i])

for hi in range(1, num2 + 1):
    if num2 % hi == 0:
        list2.extend([hi])


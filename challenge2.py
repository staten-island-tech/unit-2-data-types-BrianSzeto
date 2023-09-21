bill = int(input("What was the value of the bill? "))
tip = input("How was the service? ")
if tip == "bad":
    total = bill * 1
if tip == "okay":
    total = bill * 1.15
if tip == "good":
    total = bill * 1.20
if tip == "great":
    total = bill * 1.25

print(total)
eastbound = input("Eastbound traffic: True or False ")
westbound = input("Westbound traffic: True or False ")

printfalse = "False"
printtrue = "True"


if eastbound == "True" and westbound == "True":
    print(printfalse)
elif eastbound == "True" and westbound == "False":
    print(printtrue)
elif eastbound == "False" and westbound == "True":
    print(printtrue)
elif eastbound == "False" and westbound == "False":
    print(printtrue)
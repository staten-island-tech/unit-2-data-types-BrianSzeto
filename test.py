usrnme = input("Username: ")
paswrd = input("Password: ")
loginscript = "You are Kitson please spam his google classrooms"
error = "You are not Kitson, go away"

def login(x,y):
    if x == "kitson.lau23" and y == "123":
        print(loginscript)
    else:
        print(error)

login(usrnme,paswrd)
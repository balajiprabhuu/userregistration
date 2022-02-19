import re


def registration():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    db = open("registrationdb.txt","r")
    print("Fill the below details to sign up:")
    username = input("Create Username: ")
    password = input("Create Password: ")

    e=[]
    f=[]

    for i in db:
        g,h=i.split(", ")
        h=h.strip()
        e.append(g)
        f.append(h)

    data=dict(zip(e,f))

    flag = 0
    while True:
        if len(password) < 5 or len(password) > 16:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@&%*#!~]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            break

    a=0

    if(re.fullmatch(regex, username)):
        a = 1

    if a == 0:
        print("Enter Valid Email Address")
        registration()
    else:
        if flag==-1:
            print("Enter Valid Password")
            registration()
        else:
            db = open("registrationdb.txt","a")
            db.write(username+", "+password+"\n")
            print("Registration Successful")


def login():
    db = open("registrationdb.txt", "r")
    username=input("Username: ")
    password=input("Password: ")

    if not len(username or password) < 1:
        e = []
        f = []

        for i in db:
            g, h = i.split(", ")
            h = h.strip()
            e.append(g)
            f.append(h)

        data = dict(zip(e, f))

        try:
            if data[username]:
                try:
                    if password==data[username]:
                        print("Login Successful!")
                        print("Hi, ",username)
                    else:
                        print("Incorrect Password\n")
                        print("Enter 1 for Relogin")
                        print("Enter 2 for Forgot Password")
                        option = int(input("Enter Your Option: "))
                        if option == 1:
                            login()
                        elif option == 2:
                            forgotpassword()
                        else:
                            print("Enter a Value")
                except:
                    print("Incorrect Username or Password")
            else:
                print("Incorrect Username")
        except:
            print("Username Does Not Exist")
            print("Enter 1 for Register")
            print("Enter 2 for Relogin")
            option = int(input("Enter Your Option: "))
            if option == 1:
                registration()
            elif option == 2:
                login()
            else:
                print("Enter a Value")
    else:
        print("Enter a Value")

def home(option=None):
    print("Enter 1 for Login")
    print("Enter 2 for Signup")
    print("Enter 3 for Forgot Password")
    print("\n")
    option = int(input("Enter Your Option: "))
    if option == 1:
        login()
    elif option == 2:
        registration()
    elif option ==3:
        forgotpassword()
    else:
        print("Enter a Value")

def forgotpassword():
    db = open("registrationdb.txt", "r")
    username = input("Username: ")

    if not len(username) < 1:
        e = []
        f = []

        for i in db:
            g, h = i.split(", ")
            h = h.strip()
            e.append(g)
            f.append(h)

        data = dict(zip(e, f))

        try:
            if data[username]:
                print("Your password is ",data[username])
            else:
                print("Incorrect Username")
        except:
            print("Enter a valid username")
    else:
        print("Enter a value")



home()

















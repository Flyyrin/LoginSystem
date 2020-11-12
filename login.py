def login():
    username = input("Username: ")
    password = input("Password: ")
    PI = open("F:\python\projects\Login\data.txt", "r")
    for line in PI.readlines():
        login_info = line.split()
        if username in login_info and password in login_info:
            index = login_info.index(username)+1
            user_pass = login_info[index]
            if user_pass == password:
                return("You logged in Welcome "+ username)
            else:
                return("Wrong Username or Password")
        else:
             return("Wrong Username or Password")        
    PI.close          


def register():
         PI = open("F:\python\projects\Login\data.txt", "r")
         username = input("Create a new username:   ")  
         password = input("Create a new password:   ")
         passwordR = input("Confirm Password:   ")
         ready_for_write = False
         if password == passwordR:
            for line in PI.readlines():
                login_info = line.split()
                if username in login_info:
                    return("There is already a account with the username "+ username)
                else:
                    ready_for_write = True
         else:
             return("You did not Enter the same password twice.") 
         PI.close()    
         if ready_for_write == True:
             PIA = open("F:\python\projects\Login\data.txt", "a")
             PIA.write(username)
             PIA.write(" ")
             PIA.write(password)
             PIA.write(" ")
             PIA.close()
             print("Account was Succsesfully created.\nYou may log in now.")
             return(login())

         
                         



print("Enter:")
print("L to login.")
print("R to Register.")
choise = input("Enter choise:   ")
if choise is "L" or choise is "R":
    if choise == "L":
        print(login())  
    else:
        print(register())
else:
    print("Follow the instructions.")            





       
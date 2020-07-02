#program for text based login/account creation application using files
"""
1. ask if the user wants to login or create account
2. if create account, ask for details, store details in file.
        - Verify userid format
        - verify pswrd format
        - confirm password
3. if login, check credentials, if not present say invalid credentials


"""

import re
import json
import os
import shutil

#Functions

#function to check validity and availability of UserID
def checkuserid(userid,udict):
    match = 0
    count = 0
    pattern = "\w{3,6}"
    matchuser = re.match(pattern,userid)
    if matchuser:
        match += 1
    if userid not in udict:
        count += 1

    if match == 1 and count == 1:
        return True
    else:
        return False

#function to check validity of password
def pswrdformat(pswrd):
    #match = 0
    pattern = "^(?=.{6,8})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    matchpswrd = re.match(pattern,pswrd)
    if matchpswrd:
        #match += 1
        return True
    else:
        return False

#Main program        
print ("Hello!")
print('Would you like to Login or Create an Account?')
choice = input('(Create Account/Login)\n')

#For creators of new account
if choice.casefold() == "create account":
    with open("credentials.txt", "r") as file:
        data = file.read()
        dict2 = json.loads(data)
        file.close()
        
    #Entering User ID
    print("User ID Should be 3 to 6 Alphanumeric characters")
    uservalidity = False
    while not uservalidity:
            
        userid = input('Enter User ID\n')
        check_user = checkuserid(userid,dict2)
        if check_user:
            print ("Valid Username\n")
            uservalidity = True
        else:
            print ("Incorrect Format or UserID exists\n")

    #Entering pswrd
    print ("Password format is of 6 to 8 characters containing atleast one uppercase, one lowercase and one special character.")
    pswrdvalid = False
    while not pswrdvalid:
        pswrd = input("Enter password\n")
        check_pswrd = pswrdformat(pswrd)
        if check_pswrd:
            pswrdvalid = False
            print('Good Password')
            break
        else:
            print('Password does not meet all requirements\n')

    #Confirming Password
    pswrdconfirm = False
    confirm_pswrd = input('Re-enter password for confirmation\n')
    while not pswrdconfirm:
        if pswrd == confirm_pswrd:
            pswrdconfirm = True
        else:
            print('Passwords do not match. Re-enter password\n')
                
    #Entering Username and Passwords in the file
    with open (r"temp_file.txt", "w+") as temp_file:
            
        #dict1 = json.loads(line)
        #print(dict1)
        path = r"C:/Users/mahev/Downloads/Python Files/"
        dict2.update({userid:pswrd})
        temp_file.write(str(dict2))
        temp_file.close()
    shutil.move(r"temp_file.txt",r"credentials.txt")

    print(f"New Account with UserID {userid} was created successfully.")        
    

elif choice.casefold() == "login":
    userid = input("Enter UserID\n")
    pswrd = input("Enter Password\n")
    logincheck = 0
    login_bool = True
    with open(r"credentials.txt", "r") as file:
        data = file.read()
        dict1 = json.loads(data)
        print(dict1.items())
        
    while login_bool:
        for key,value in dict1.items():
            if dict1[userid] == pswrd:
                logincheck += 1
        if logincheck:
            print("Login Successful")
            login_bool = False
        else:
            print("Incorrect credentials. Please re-enter.")
            userid = input("Enter UserID\n")
            pswrd = input("Enter Password\n")

else:
    print(f"{choice} Choice does not available.")
        
                


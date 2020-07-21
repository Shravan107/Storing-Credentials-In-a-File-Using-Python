import os.path

def encode(p):
    key = len(p)
    x = p[::-1] + str(key)
    return x
    
def delFile():
  if os.path.exists("info.txt"): 
      os.remove("info.txt")  
      print("File deleted !")
      exit(0)  
  else: 
      print("File doesnot exist !")
      exit(0) 

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

def appendNew():
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = encode(input("Please enter the password here: "))
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)

checkExistence()
while True:
    x = input("Enter option:  'n': new password 'r': show password 'd': delete file 'q': quit --->" )
    if (x == 'q'):
        exit(0)
    elif (x == 'n'):
        appendNew()
    elif (x == 'r'):
        readPasswords()
    elif (x == 'd'):
        delFile()
    else :
      print("Incorrect key!")


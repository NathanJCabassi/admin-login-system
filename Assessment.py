import csv


def mainmenu():
	print("""
		Main Menu
		Welcome Administrator. What would you like to do?

		A) Login as user
		B) Create a user
		C) Delete a user
		D) Exit the program
		""")
	selection = input("enter a, b, c, or d, to select it: ")
	selection = selection.lower() #as the if statement is case sensitive i use this to set everything the user 
	if selection == "a":
		print ("you have selected to login")
		main()
	elif selection == "b":
		createusercheck()
	elif selection == "c":
		print("you have selected to delete a user")
		admindeleteuser()
	elif selection == "d":
		print ("you have selected to exit the program")
	else:
		print ("that is not an option try again")
		mainmenu()

def createusercheck():
	with open("users.txt","r") as file:
		file_reader = csv.reader(file)
		createuser(file_reader)
		file.close()

def createuser(file):
    user = input("Enter your username: ")
    user = user.lower()
    for row in file:
        if row[0] != user:
            print("username username available", user)
            createpass(user)
            break
        else:
            print("username is already in use please try again")
            mainmenu()

def createpass(username):
	password = input ("what will the password be: ")
	users = open ("users.txt","a+")
	users.write("\n")
	users.write(username + "," + password)
	users.close()
	print ("User has been created")
	print ("you can now login as: " + username)
	mainmenu()


def main():
    with open("users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()
 
def user_find(file_reader):
    user = input("Enter your username: ")
    user = user.lower()
    for row in file_reader:
    	if row[0] == user:
            print("username found", user)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            break
 
def pass_check(user_found):
    user = input("enter your password: ")
    if user_found[1] == user:
        print("password match you have now logged in as: "+ user_found[0])
        user_menu(user_found)
    else:
        print("password not match")


def user_menu(user_found):
	print("Welcome " + user_found[0] + "what would you like to do")
	print("""
		A) Change Password
		B) Delete Account
		C) Sign out
		""")
	selection = input("enter a, b, or c, to select it: ")
	selection = selection.lower() #as the if statement is case sensitive i use this to set everything the user 
	if selection == "a":
		print ("you have chosen to change your password")
		passwordchange(user_found)
	elif selection == "b":
		print("you have chosen to delete your account")
		user_delete(user_found)
	elif selection == "c":
		print("you have chosen to sight out")
		mainmenu()
	else:
		print ("that is not an option try again")
		user_menu(user_found)

def user_delete(user_found):
	lines = ["0", "1"]
	lines.remove("0")
	lines.remove("1")
	usernamepass = user_found[0] + "," + user_found[1]
	members= input("Please enter a your name to confirm ")
	if members != user_found[0]:
		print ("that is not your username try again")
		user_delete(user_found)
	with open('users.txt', 'r') as readFile:
		reader = csv.reader(readFile)
		readFile.close
		for row in reader:
			rowuserpass = row[0] + "," + row[1]
			lines.append(rowuserpass)
	lines.remove(usernamepass)
	if usernamepass != ("admin,admin"):
		lines.remove("admin,admin")
	x = len(lines)
	i=0
	writeFile = open('users.txt', 'w')
	writeFile.write("admin,admin")
	writeFile.close
	while True:
		if i<x:
			writeFile = open('users.txt', 'a+')
			writeFile.write("\n")
			writeFile.write(lines[i])
			writeFile.close
			i = i+1
		elif i==x or i>x:
			mainmenu()
			break
		



def admindeleteuser():
	print("please enter everything carefully as the user must exist:")
	user = input("Enter users username: ")
	password = input ("enrer users password: ")
	user = user.lower()
	user_found = [user,password]
	user_delete(user_found)

def passwordchange(user_found):
	if user_found[0] == "admin":
		print("admin password can not be changed")
		mainmenu()
	elif user_found[0] != "admin":
		lines = ["0", "1"]
		lines.remove("0")
		lines.remove("1")
		members= input("Please enter a your name to confirm: ")
		password = input ("please input your current password: ")
		newpassword = input ("please input your new password: ")
		usernamepass = user_found[0] + "," + user_found[1]
		newuernamepass = user_found[0] + "," + newpassword
		if members != user_found[0] or password != user_found[1]:
			print ("that is not your username or password try again")
			user_menu(user_found)
		with open('users.txt', 'r') as readFile:
			reader = csv.reader(readFile)
			readFile.close
			for row in reader:
				rowuserpass = row[0] + "," + row[1]
				lines.append(rowuserpass)
				print(lines)
			readFile.close
		lines.remove(usernamepass)
		if usernamepass != ("admin,admin"):
			lines.remove("admin,admin")
		lines.append(newuernamepass)
		x = len(lines)
		i=0
		writeFile = open('users.txt', 'w')
		writeFile.write("admin,admin")
		writeFile.close
		while True:
			if i<x:
				writeFile = open('users.txt', 'a+')
				writeFile.write("\n")
				writeFile.write(lines[i])
				writeFile.close
				i = i+1
			elif i==x or i>x:
				print("your password has been changed the program must be restarted to edit the user again")
				mainmenu()
				break

mainmenu()

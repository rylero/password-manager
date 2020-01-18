from tkinter import *

root = Tk()

rowHigh = 7


#func
def startup():
	global rowHigh

	f = open("passwordTextFile.txt", "r")
	for line in f:
		data = line.split()

		nameText = data[0]
		usernameText = data[1]
		emailText = data[2]
		passwordText = data[3]

		NameLabel_sub = Label(root, text=nameText)
		UserNameLabel_sub = Label(root, text=usernameText)
		EmailLabel_sub = Label(root, text=emailText)
		PasswordLabel_sub = Label(root, text=passwordText)
		Spacer2 = Label(root, text="        ")
		DeleteButton = Button(root, text="X", bg="red", command=deleteline)

		rowHigh+= 1

		NameLabel_sub.grid(column=1,row=rowHigh)
		UserNameLabel_sub.grid(column=2,row=rowHigh)
		EmailLabel_sub.grid(column=3,row=rowHigh)
		PasswordLabel_sub.grid(column=5,row=rowHigh)
		Spacer2.grid(column=4, row=rowHigh)
		DeleteButton.grid(column=7, row=rowHigh)

def deleteline():
	#try to delete line
	print("deleted")


	

def submitForm():
	global rowHigh
	nameText = NameEntry.get()
	usernameText = UserNameEntry.get()
	emailText = EmailEntry.get()
	passwordText = PasswordEntry.get()

	f = open("passwordTextFile.txt", "a")
	f.write(nameText+" "+usernameText+" "+emailText+" "+passwordText)
	f.write("\n")
	f.close()
	NameLabel_sub = Label(root, text=nameText)
	UserNameLabel_sub = Label(root, text=usernameText)
	EmailLabel_sub = Label(root, text=emailText)
	PasswordLabel_sub = Label(root, text=passwordText)
	Spacer2 = Label(root, text="        ")
	DeleteButton = Button(root, text="X", bg="red", command=deleteline)

	rowHigh+= 1

	NameLabel_sub.grid(column=1,row=rowHigh)
	UserNameLabel_sub.grid(column=2,row=rowHigh)
	EmailLabel_sub.grid(column=3,row=rowHigh)
	PasswordLabel_sub.grid(column=5,row=rowHigh)
	Spacer2.grid(column=4, row=rowHigh)
	DeleteButton.grid(column=7, row=rowHigh)

	PasswordEntry.delete(0, END)
	PasswordEntry.insert(0, "")

	EmailEntry.delete(0, END)
	EmailEntry.insert(0, "")

	UserNameEntry.delete(0, END)
	UserNameEntry.insert(0, "")

	NameEntry.delete(0, END)
	NameEntry.insert(0, "")



#read file
startup()

#button
SubmitButton = Button(root, text="Submit", command=submitForm)
#labls
NameLabel = Label(root, text="Name:")
UserNameLabel = Label(root, text="UserName:")
EmailLabel = Label(root, text="Email:")
PasswordLabel = Label(root, text="Password:")

BottomNameLabel = Label(root, text="Name")
BottomUserNameLabel = Label(root, text="UserName")
BottomEmailLabel = Label(root, text="Email")
BottomPasswordLabel = Label(root, text="Password")

Spacer = Label(root, text="        ")
Spacer1 = Label(root, text="     ")

#entry
NameEntry = Entry(root)
UserNameEntry = Entry(root)
EmailEntry = Entry(root)
PasswordEntry = Entry(root)

#put stull on screen
NameLabel.grid(column=1, row=1)
NameEntry.grid(column=2, row=1)

UserNameLabel.grid(column=1, row=2)
UserNameEntry.grid(column=2, row=2)

EmailLabel.grid(column=1, row=3)
EmailEntry.grid(column=2, row=3)

PasswordLabel.grid(column=1, row=4)
PasswordEntry.grid(column=2, row=4)

BottomNameLabel.grid(column=1, row=7)
BottomUserNameLabel.grid(column=2, row=7)
BottomEmailLabel.grid(column=3, row=7)
BottomPasswordLabel.grid(column=5, row=7)

Spacer.grid(column=4, row=7)
Spacer1.grid(column=1, row=6)

SubmitButton.grid(column=2, row=5)

root.mainloop()
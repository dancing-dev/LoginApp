from tkinter import *
import string
from random import *
root = Tk()
root.title("Employee Management System")
root.geometry("500x185")


registerEntry = Entry(root)
registerButton = Button(root, text="Register Your Account", command = lambda: register())
registerLabel = Label(root, text="Enter name to register:")




loginEntry = Entry(root)
loginButton = Button(root, text="Login", command = lambda: login())
loginLabel = Label(root, text="Name for login:")
loginNum = Entry(root)



registerButton.place(x=157, y=25)
registerEntry.place(x=160, y=0)
registerLabel.place(x=0, y=0)


loginButton.place(x=200, y=150)
loginEntry.place(x=160, y=100)
loginLabel.place(x=0, y=100)
loginNum.place(x=160, y=125)
accountNum = " "






def register():
	registerName = (registerEntry.get())
	
	accountNum = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))


	Account_txt = open("Accounts.txt", "a")
	Account_txt.write(registerName + accountNum + "\n")
	Account_txt.close()
	print("[System] Made Account")
	registerEntry.delete(0, 'end')
	openApp(registerName, accountNum)
	




def login():
	loginCombo = loginEntry.get() + loginNum.get()

	with open("Accounts.txt", "r") as a:
		if loginCombo in a.read():
			accountName = loginEntry.get()
			print("[System] Found Account")
			openApp(accountName, loginNum.get())
		else:
			print("[System] No Account found")
			loginEntry.delete(0, 'end')

def openApp(account, num):
	
	app = Toplevel(root)
	app.geometry("500x500")

	numLabel = Label(app, text=num)
	labelForNum =Label(app, text="This is your password: ")

	labelForNum.place(x=0, y= 450)
	numLabel.place(x=150, y= 450)
	


	

root.mainloop()

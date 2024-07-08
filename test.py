from tkinter import *

root = Tk()
root.title("Our First Window")
root.geometry("500x700")
root.maxsize(600, 800)
root.minsize(200, 400)
root["height"] = 500
root["bg"] = "purple"
root["cursor"] = "heart"

def printText(event):
    print(event)

def doSomething(event):
    label1 = Label(root, text="No")
    label1.bind("<Button-1>", printText)
    label1.pack()

btn1 = Button(root, text="Let's talk about love")
btn1.place(relx=0.5, rely=0.5, anchor="center")
btn1.bind("<Button-1>", doSomething)

entry = Entry(font="Tahoma 20")
entry.pack(pady=15, padx=15)

EntryBtn = Button(root, text="Check My Password")
EntryBtn.pack()

def printInputs(event):
    print(entry.get())
EntryBtn.bind("<Button-1>", printInputs)

labelSuccess = Label(text="")
labelSuccess.pack()

def validatePassword(event):
    textInTheEntry = entry.get()
    password = "123456"
    if textInTheEntry == password:
        for widget in root.winfo_children():
            widget.destroy()
        label = Label(text="Welcome to the chatroom", font="Tahoma 20")
        label["bg"] = "gray"
        label.pack()
    else:
        labelSuccess.config(text="Password is incorrect")
EntryBtn.bind("<Button-1>", validatePassword)

root.mainloop()

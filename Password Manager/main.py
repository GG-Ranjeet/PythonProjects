from tkinter import messagebox
from tkinter import *
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for n in range(nr_letters)]
    [password_list.append(random.choice(numbers)) for n in range(nr_numbers)]
    [password_list.append(random.choice(symbols)) for n in range(nr_symbols)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
text = ''
def save_password():
    global text

    if website_entry.get()=='' or email_entry.get()=='' or password_entry.get()=='':
        messagebox.showwarning(title="Something went wrong!", message='Dont leave the field Empty')
    else:
        text = f'{website_entry.get().lower()} | {email_entry.get()} | {password_entry.get()}\n'
        is_ok = messagebox.askokcancel(title="Save Password?", message=f"You entered the following details: \nEmail:{email_entry.get()} \nPassword: {password_entry.get()}")
        if is_ok:
            with open('password.txt', 'a') as file:
                file.write(text)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

def add_gmail():
    email_entry.insert(END, '@gmail.com')

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.config(padx=20, pady=20)
windows.geometry('450x400')
windows.title("Password Manager")

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100,100 ,image=photo)
canvas.grid(row=0,column=1)

website_label = Label(text='website:')
website_label.grid(row=1,column=0,sticky= 'e')
email_label = Label(text = 'Email/Username:')
email_label.grid(row=2,column=0,sticky= 'e')
password_label = Label(text='Password:')
password_label.grid(row=3,column=0, sticky= 'e')

website_entry = Entry()
website_entry.grid(row=1,column=1, columnspan=2, sticky='we')
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2,column=1, columnspan=1, sticky='we')
password_entry = Entry()
password_entry.grid(row=3,column=1, sticky='we')

button = Button(text='Generate Password', command=generate_password)
button.grid(row=3,column=2, sticky='we')
add_button = Button(text='@gmail.com?', command=add_gmail)
add_button.grid(row=2,column=2, sticky='we')
save_button = Button(text='Add Password', command=save_password)
save_button.grid(row=4,column=1,columnspan=2, sticky='we')

windows.mainloop()
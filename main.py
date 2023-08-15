from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip

FILL_ALL = "Please fill out all fields"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, f"{password}")
    # pyperclip.copy(password)
    # saves the generated password straight to your clipboard to paste straight away
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry
    password = password_entry
    username = username_entry

    # print(website_entry.get())

    if (website.get() == "") or website.get().isspace():
        messagebox.showerror(title=f"Error", message=f"{FILL_ALL}" )
    elif (username.get() == "") or username.get().isspace():
        messagebox.showerror(title=f"Error", message=f"{FILL_ALL}")
    elif (password.get() == "") or password.get().isspace():
        messagebox.showerror(title=f"Error", message=f"{FILL_ALL}")
    else:
        is_ok = messagebox.askokcancel(title=website.get(), message=f"Username: {username.get()}\n "
                                                        f"Password: {password.get()}\n Are is it okay to save?")
        if is_ok:
            with open("passwords", mode="a") as passwords:
                passwords.write(f"{website.get()} | {username.get()} | {password.get()} \n")
                website.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Website row
website_label = Label(text="Website:")
website_label.grid(column=0,row=1, sticky=E)
website_entry = Entry(width= 43)
website_entry.focus()
website_entry.grid(column=1, row= 1, sticky=E,  columnspan=2, pady=2)

# Username row
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, sticky=E)
username_entry = Entry(width= 43)
username_entry.insert(0, "nmwasuku@yahoo.co.uk")
username_entry.grid(row=2, column=1, columnspan=2, sticky=E)

# Password row
password_label = Label(text="Password:")
password_label.grid(column=0, row=3,sticky=E)
password_entry = Entry(width= 24)
password_entry.grid(row=3, column=1, sticky=E, padx=7)
gen_pass_button = Button(text="Generate Password", width=14, command=generate_password)
gen_pass_button.grid(row=3, column=2, pady=2)

# Add
add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1, columnspan=2, sticky=E)




window.mainloop()


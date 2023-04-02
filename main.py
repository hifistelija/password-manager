from tkinter import *
from tkinter import messagebox
import random
import string


def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&()*+"

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)]
        + [random.choice(numbers) for _ in range(nr_numbers)]
        + [random.choice(symbols) for _ in range(nr_symbols)]
    )

    random.shuffle(password_list)
    password = "".join(password_list)

    # Update entry_password widget with the generated password
    entry_password.delete(0, END)
    entry_password.insert(0, password)

    # Copy password to the clipboard or use pyperclip module
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()  # Ensures the clipboard to update immediately


def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not (website and username and password):
        messagebox.showwarning(title="Warning", message="Please make sure all fields are filled")
        return

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nUsername: {username}'
                                                          f'\nPassword: {password} \nIs it ok to save?')

    if is_ok:
        formatted_data = f"{website} | {username} | {password}\n"

        with open("passwords.txt", "a") as file:
            file.write(formatted_data)

        # Clear the input fields
        entry_website.delete(0, END)
        entry_password.delete(0, END)

        messagebox.showinfo(title="Success", message="Password was saved successfully!")


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=39)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_username = Entry(width=39)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "ilkka.heino29@outlook.com")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=31, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()

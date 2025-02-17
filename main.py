import tkinter
import random
from tkinter import messagebox
import pyperclip
import json
email = "jakeeb05@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    epassword.delete(0, tkinter.END)
    password = []
    length = random.randint(8,12)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}']
    nums =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for _ in range(length):
        list_selection = random.randint(0,2)
        if list_selection == 0:
            password.append(random.choice(letters))
        if list_selection == 1:
            password.append(random.choice(symbols))
        if list_selection == 2:
            password.append(random.choice(nums))

    final_pass = "".join(password)
    epassword.insert(0, string=final_pass)   

    pyperclip.copy(final_pass) 


def find_password():
    website = ewebsite.get().title()
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)

        password = data[website]["password"]
        pop_up = messagebox.showinfo(title=website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
    except KeyError:
        pop_up = messagebox.showinfo(title=website, message=f"No information found for '{website}'")
    except FileNotFoundError:
        pop_up = messagebox.showinfo(title=website, message=f"No information found for '{website}'\nNo data stored yet")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_entry():
    website_entry = ewebsite.get().title()
    password_entry = epassword.get().title()
    
    new_dict = {
        website_entry: { 
            "email" : email,
            "password": password_entry
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0:
        pop_up = messagebox.showwarning(title="Oops", message="Please dont leave any fields empty")
        return
    else:
        try:
            with open(file="data.json", mode="r") as file:
                #read old data
                data = json.load(file)
                #update old data with new data
                data.update(new_dict)
            with open(file="data.json", mode="w") as file:
                #save updated data
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_dict, file, indent=4)
        ewebsite.delete(0, tkinter.END)
        epassword.delete(0,tkinter.END)
        ewebsite.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_img = tkinter.PhotoImage(file="logo.png")
logo_canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0,column=1)

lwebsite = tkinter.Label(text="Website")
lwebsite.grid(row=1, column=0)
ewebsite = tkinter.Entry(width=18)
ewebsite.grid(row=1, column=1, columnspan=1)
ewebsite.focus()

lusername = tkinter.Label(text="Email/Username: ")
lusername.grid(row=2, column=0)
eusername = tkinter.Entry(width=35)
eusername.grid(row=2, column=1, columnspan=2)
eusername.insert(0, string=email)

lpassword = tkinter.Label(text="Password")
lpassword.grid(row=3, column=0)
epassword = tkinter.Entry(width=18)
epassword.grid(row=3, column=1)

genpass_button = tkinter.Button(text="Generate Password", command=generate_password)
genpass_button.grid(row=3, column=2)
        
add_button = tkinter.Button(text="Add", width=33, command=get_entry)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()
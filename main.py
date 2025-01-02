import tkinter
import random
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

# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_entry():
    website_entry = ewebsite.get()
    password_entry = epassword.get()
    final_entry = website_entry + " | " + email + " | " + password_entry + "\n"

    with open(file="data.txt", mode="a") as file:
        file.write(final_entry)

    ewebsite.delete(0, tkinter.END)
    epassword.delete(0,tkinter.END)

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
ewebsite = tkinter.Entry(width=35)
ewebsite.grid(row=1, column=1, columnspan=2)
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


window.mainloop()
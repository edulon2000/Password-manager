from tkinter import*
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)
    
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get()
    user = entry_user.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email": user,
            "password": password,
    }
}
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Please don't leave any fields empty!")
    else:
        try:
            with open("password-manager\data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password-manager\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("password-manager\data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0,END)
def search():
    website = entry_website.get()
    try:
        with open("password-manager\\data.json") as data_file:
                # reading old data
                data_json = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")  
    else:
        if website in data_json:
            messagebox.showinfo(title=f"{website}", message=f"Email:{data_json[website]["email"]}\nPassword: {data_json[website]["password"]}")
        else:
            messagebox.showerror(title="Error", message=f"No Details for {website} exists")  
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="password-manager\logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=0,row=0,columnspan=2)

# labels
label_website = Label(text="Website:", font=("Courier",15))
label_website.grid(column=0,row=2,sticky="e")
label_user = Label(text="Email/Username:", font=("Courier",15))
label_user.grid(column=0,row=3,sticky="e")
label_password = Label(text="Password:", font=("Courier",15))
label_password.grid(column=0,row=4,sticky="e")

# entrys
entry_website = Entry(width=21)
entry_website.grid(column=1,row=2,sticky="w")
entry_website.insert(0,"www.teste.com.br")

entry_user = Entry(width=36)
entry_user.grid(column=1,row=3,sticky="w")
entry_user.insert(0,"edu@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1,row=4,columnspan=1,sticky="w")
entry_password.insert(0,"12345")

# buttons
button_generate_password = Button(text= "Generate Password",width=15,command=generate_password)
button_generate_password.grid(column=1,row=4,columnspan=1,sticky="e")

button_add = Button(text= "Add",width=36,command= add)
button_add.grid(column=1,row=5,columnspan=1)

button_add = Button(text= "Search",width=15,command= search)
button_add.grid(column=1,row=2,columnspan=2,sticky="e")

window.mainloop()
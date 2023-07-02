import random
import string
import tkinter as tk
from tkinter import *

# GUI design
root = Tk()
root.title("PassArmor: Safeguarding Your Digital Identity")
root.resizable(False, False)
root.geometry("700x500+500+200")
root.configure(bg="black")

# Icon
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)

# Logo
logo = PhotoImage(file="logo1.png")
Label(root, image=logo, bg="black").place(x=175, y=7)
Label(root, text="PassArmor", bd=3, bg="black", fg="red", font="arial 30 bold").place(x=270, y=20)
Label(root, text="Safeguarding Your Digital Identity", bg="black", fg="white", font="arial 7").place(x=300, y=65)
Label(root, text="\" Check password's strength and ensure it hasn't been publicly leaked \"", bd=3, bg="black",
      fg="yellow", font="arial 10 bold").place(x=120, y=110)

# Password label
pass_label = tk.Label(root, text="Password:", bd=5, fg="white", bg="black", font="arial 15 bold")
pass_label.place(x=195, y=170)

# Text box
text_box = tk.Entry(root, show="*", bd=5, fg="black", bg="white", font="arial 15 bold")
text_box.place(x=310, y=170)

# Check button
check_button = tk.Button(root, text="Check", font="arial 15 bold", command=lambda: check_password(text_box.get()))
check_button.place(x=200, y=250)

# Show button
show_button = tk.Button(root, text="Show ", font="arial 15 bold", command=lambda: show_pass(text_box))
show_button.place(x=300, y=250)

generate = tk.Button(root, text="Auto-Generate", font="arial 15 bold", command=lambda: generate_password(text_box))
generate.place(x=400, y=250)

# Result label
result_label = tk.Label(root, text="", bd=5, font="arial 13 bold")
result_label.place(x=180, y=330)


def show_pass(password_entry):
    password_entry.config(show="")


# Auto generate password
def generate_password(password_entry):
    length = 18
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(chars)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)


# Check for password Strength
def check_strength(password):
    min_len = 8
    number = False
    letter = False
    spec_char = False
    mix_char = False

    if len(password) >= min_len:  # check for length
        for char in password:
            if char.isdigit():  # check for digits
                number = True
                break

        for char in password:
            if char.isalpha():  # check for letters
                letter = True
                break

        for char in password:
            if char in string.punctuation:  # check mixture for digits, special characters and numbers
                spec_char = True
                break

        mix_char = number and letter and spec_char

    if len(password) < min_len:
        strength = "\u26A0 WEAK: Password is too short."

    elif not number:
        strength = "\u26A0 WEAK: Password must contain letters, \n numbers & special-characters."

    elif not letter:
        strength = "\u26A0 WEAK: Password must contain letters, \n numbers & special-characters."

    elif not mix_char:
        strength = "\u26A0 WEAK: Password must contain letters, \n numbers & special-characters."

    else:
        strength = "\u2713 STRONG: Password meets all strength criteria."

    return strength


# Check for password leakage
def check_password_leakage(password):
    file = open("leak.txt", "r")  # Open file in reading mode
    leaked_passwords = file.readlines()  # Read file content
    leaked_passwords = [line.strip() for line in leaked_passwords]  # Remove the newline character from each line and store in a new list

    if password in leaked_passwords:
        return "\u26A0 CAUTION: Password is publicly leaked."

    else:
        return "\u2713 Password doesn't found in public leaks.\n It's good to use"

    file.close()


# Integrating Password Strength and Leakage Checks
def check_password(password):
    strength_result = check_strength(password)
    leakage_result = check_password_leakage(password)

    result_message = "{}\n \n {}".format(strength_result, leakage_result)
    result_label.configure(text=result_message)


root.mainloop()

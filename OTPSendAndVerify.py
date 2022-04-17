import string
from tkinter import *
from tkinter import messagebox
import smtplib
import random
import math
import os

root = Tk()
root.title("Send OTP Via Email")
root.geometry("565x250")
email_label = Label(root, text="Enter receiver's Email: ",
                    font=("ariel 15 bold"), relief=FLAT)
email_label.grid(row=0, column=0, padx=15, pady=60)
email_entry = Entry(root, font=("ariel 15 bold"),
                    width=25, relief=GROOVE, bd=2)
email_entry.grid(row=0, column=1, padx=12, pady=60)
email_entry.focus()


string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lent=len(string)
otp = ""
for i in range(6):
    otp += string[math.floor(random.random() * lent)]
file2 = open("otp.txt", "w")
file2.write(otp)
file2.close()


def send():
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        s.starttls()
        s.login("d21dcs159@charusat.edu.in", "olnrdgynmkbyuhdk")
        s.sendmail("d21dcs159@charusat.edu.in", email_entry.get(), 'Your OTP Verification for app is ' +
                   otp+' Note..  Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid')
        messagebox.showinfo("Send OTP via Email",f"OTP sent to {email_entry.get()}")
        s.quit()
        os.system('python second.py')
    except:
        messagebox.showinfo(
            "Send OTP via Email", "Please enter the valid email address OR check an internet connection")


send_button = Button(root, text="Generate OTP", font=(
    "ariel 15 bold"), bg="black", fg="white", bd=5, command=send)
send_button.place(x=210, y=150)
root.mainloop()

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Student Registration Form")
root.geometry("450x400")
root.config(bg="lightblue")
def register():
    if name_var.get() == "" or email_var.get() == "" or phone_var.get() == "" or password_var.get() == "" or gender_var.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        messagebox.showinfo("Success", "Registration Successful")
        print("Name:", name_var.get())
        print("Email:", email_var.get())
        print("Phone:", phone_var.get())
        print("Password:", password_var.get())
        print("Gender:", gender_var.get())
def only_numbers(char):
    return char.isdigit()
validate_num = root.register(only_numbers)
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
password_var = StringVar()
gender_var = StringVar()
Label(root, text="REGISTRATION FORM", font=("Arial", 16, "bold"), bg="lightblue").grid(row=0, column=1, pady=15)
Label(root, text="Full Name", bg="lightblue").grid(row=1, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=name_var).grid(row=1, column=1)
Label(root, text="Email ID", bg="lightblue").grid(row=2, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=email_var).grid(row=2, column=1)
Label(root, text="Phone Number", bg="lightblue").grid(row=3, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=phone_var, validate="key",
      validatecommand=(validate_num, "%S")).grid(row=3, column=1)
Label(root, text="Password", bg="lightblue").grid(row=4, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=password_var, show="*").grid(row=4, column=1)
Label(root, text="Gender", bg="lightblue").grid(row=5, column=0, padx=10, pady=5, sticky=W)
Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="lightblue").grid(row=5, column=1, sticky=W)
Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="lightblue").grid(row=5, column=1)
Button(root, text="Register", command=register, width=15, bg="green", fg="white").grid(row=6, column=1, pady=20)
root.mainloop()

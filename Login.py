import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Homepage import Homepage
from CreateAcc import CreateAcc  # Assuming CreateAcc is a class

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("PUP Login System")
        self.root.geometry("800x400")
        self.root.configure(bg="#add8e6")  # Light blue background

        self.create_widgets()

    def create_widgets(self):
        # Load and display logo
        try:
            self.logo_image = Image.open(
                r"C:\Users\jurie qt\Desktop\Reco\python\494571200_698141445951733_3348868030050292808_n.jpg")
            self.logo_image = self.logo_image.resize((100, 60))
            self.logo = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(self.root, image=self.logo, bg="#add8e6")
            self.logo_label.place(x=20, y=20)
        except Exception as e:
            print(f"Error loading logo: {e}")

        # Greeting (left side)
        self.greeting_label = tk.Label(self.root, text="Good Day Pupians!", font=("Times new roman", 30), bg="#add8e6")
        self.greeting_label.place(x=70, y=150)

        # Login Frame
        self.login_frame = tk.Frame(self.root, bg="white", highlightbackground="#8a1538", highlightthickness=2)
        self.login_frame.place(x=450, y=50, width=300, height=300)

        self.welcome_label = tk.Label(self.login_frame, text="WELCOME PUP-IANS !", font=("Arial", 14, "bold"),
                                      fg="#8a1538", bg="white")
        self.welcome_label.pack(pady=10)

        self.create_username_field()
        self.create_password_field()
        self.create_login_button()
        self.create_forgot_password_link()
        self.create_create_account_button()

    def create_username_field(self):
        self.username_label = tk.Label(self.login_frame, text="Username:", bg="white")
        self.username_label.pack(anchor="w", padx=20)
        self.username_entry = tk.Entry(self.login_frame, width=30, bd=2, relief="groove")
        self.username_entry.pack(pady=5)

    def create_password_field(self):
        self.password_label = tk.Label(self.login_frame, text="Password:", bg="white")
        self.password_label.pack(anchor="w", padx=20)
        self.password_entry = tk.Entry(self.login_frame, width=30, bd=2, relief="groove", show="*")
        self.password_entry.pack(pady=5)

    def create_login_button(self):
        self.login_button = tk.Button(self.login_frame, text="Log In", bg="#8a1538", fg="white", command=self.login)
        self.login_button.pack(pady=10)

    def create_forgot_password_link(self):
        self.forgot_label = tk.Label(self.login_frame, text="Forgot Password? Click Here.", font=("Arial", 10),
                                     fg="blue", bg="white", cursor="hand2")
        self.forgot_label.pack()
        self.forgot_label.bind("<Button-1>", self.forgot_password)

    def create_create_account_button(self):
        self.create_btn = tk.Button(self.login_frame, text="Create an Account", bg="#f5b942", fg="black",
                                    command=self.create_account)
        self.create_btn.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.open_homepage(username)
        else:
            messagebox.showerror("Login Failed", "Please enter both username and password.")

    def open_homepage(self, username):
        self.root.destroy()
        homepage_window = tk.Tk()
        Homepage(homepage_window, username)
        homepage_window.mainloop()

    def create_account(self):
        self.root.destroy()
        create_account_window = tk.Tk()
        CreateAcc(create_account_window)  # Correct class instantiation
        create_account_window.mainloop()

    def forgot_password(self, event=None):
        messagebox.showinfo("Forgot Password", "Redirecting to password recovery...")

if __name__ == "__main__":
    login_window = tk.Tk()
    app = LoginSystem(login_window)
    login_window.mainloop()

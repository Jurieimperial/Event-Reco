import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure to import this for handling images

class CreateAcc:
    def __init__(self, root):
        self.root = root
        self.root.title("PUP Login System")
        self.root.geometry("800x400")
        self.root.configure(bg="#add8e6")  # Light blue background

        self.create_widgets()

    def create_widgets(self):
        # Load and display logo at the top left corner
        try:
            self.logo_image = Image.open(
                r"C:\Users\jurie qt\Desktop\Reco\python\494571200_698141445951733_3348868030050292808_n.jpg")
            self.logo_image = self.logo_image.resize((100, 60))
            self.logo = ImageTk.PhotoImage(self.logo_image)

            self.logo_label = tk.Label(self.root, image=self.logo, bg="#add8e6")
            self.logo_label.place(x=20, y=20)
        except Exception as e:
            print(f"Error loading logo: {e}")

        # Center the login frame in the window
        frame_width = 300
        frame_height = 380
        window_width = 800
        window_height = 400

        x_pos = (window_width - frame_width) // 2
        y_pos = (window_height - frame_height) // 2

        self.login_frame = tk.Frame(self.root, bg="white", highlightbackground="#8a1538", highlightthickness=2)
        self.login_frame.place(x=x_pos, y=y_pos, width=frame_width, height=frame_height)

        self.welcome_label = tk.Label(self.login_frame, text="CREATE YOUR ACCOUNT", font=("Arial", 14, "bold"),
                                      fg="#8a1538", bg="white")
        self.welcome_label.pack(pady=10)

        self.create_name_field()
        self.create_username_field()
        self.create_password_field()
        self.create_confirm_password_field()
        self.create_acc_button()
        self.back_button()

    def create_name_field(self):
        self.name_label = tk.Label(self.login_frame, text="Name:", bg="white")
        self.name_label.pack(anchor="w", padx=20)
        self.name_entry = tk.Entry(self.login_frame, width=30, bd=2, relief="groove")
        self.name_entry.pack(pady=5)

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

    def create_confirm_password_field(self):
        self.con_password_label = tk.Label(self.login_frame, text="Confirm Password:", bg="white")
        self.con_password_label.pack(anchor="w", padx=20)
        self.con_password_entry = tk.Entry(self.login_frame, width=30, bd=2, relief="groove", show="*")
        self.con_password_entry.pack(pady=5)

    def create_acc_button(self):
        self.create_acc_button = tk.Button(self.login_frame, text="Create Account", bg="#8a1538", fg="white",
                                           command=self.create_account)
        self.create_acc_button.pack(pady=10)

    def back_button(self):
        self.back_button = tk.Button(self.login_frame, text="Back", bg="#f5b942", fg="black",
                                           command=self.back)
        self.back_button.pack(pady=10)

    def create_account(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.con_password_entry.get()

        if not (name and username and password and confirm_password):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Simulate saving account (here you'd save to file or database)
        messagebox.showinfo("Success", f"Account for '{username}' has been created!")

        # Optional: open homepage or go back to login
        self.root.destroy()
        from Login import LoginSystem
        login_window = tk.Tk()
        LoginSystem(login_window)
        login_window.mainloop()

    def back(self):
        self.root.destroy()
        from Login import LoginSystem  # Ensure Login.py exists
        login_window = tk.Tk()
        LoginSystem(login_window)
        login_window.mainloop()



import tkinter as tk
from tkinter import messagebox

class Homepage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Personalized Event Recommendations")
        self.root.geometry("800x500")
        self.root.configure(bg="#e0f7fa")

        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self.root, bg="#039be5", height=80)
        top_frame.pack(fill="x")

        welcome_label = tk.Label(top_frame, text=f"Welcome, {self.username}!", font=("Arial", 18, "bold"), fg="white", bg="#039be5")
        welcome_label.pack(pady=20)

        content_frame = tk.Frame(self.root, bg="white", highlightbackground="#039be5", highlightthickness=2)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=300)

        events_label = tk.Label(content_frame, text="🎉 Recommended Events for You:", font=("Arial", 14, "bold"), bg="white", fg="#039be5")
        events_label.pack(pady=(20, 10))

        events = self.get_personalized_events(self.username)
        for event in events:
            event_label = tk.Label(content_frame, text=f"• {event}", font=("Arial", 12), bg="white", anchor="w")
            event_label.pack(pady=3, padx=20, anchor="w")

        logout_button = tk.Button(self.root, text="Log Out", bg="#039be5", fg="white", font=("Arial", 12), padx=20, pady=5, command=self.logout, relief="flat")
        logout_button.place(relx=0.9, rely=0.92, anchor="se")

    def get_personalized_events(self, username):
        return [
            "Tech Conference 2025 - May 10th",
            "Music Festival 2025 - May 15th",
            "Art Exhibition - May 20th",
            "AI Workshop - May 22nd"
        ]

    def logout(self):
        self.root.destroy()
        from Login import LoginSystem
        login_window = tk.Tk()
        LoginSystem(login_window)
        login_window.mainloop()

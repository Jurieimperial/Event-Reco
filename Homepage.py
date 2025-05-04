import tkinter as tk
from tkinter import messagebox


class Homepage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Personalized Event Recommendations")
        self.root.geometry("800x400")
        self.root.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # Welcome Message
        welcome_label = tk.Label(self.root, text=f"Welcome, {self.username}!",
                                 font=("Arial", 18, "bold"), fg="#8a1538", bg="white")
        welcome_label.pack(pady=50)

        # Personalized Event Recommendations
        events = self.get_personalized_events(self.username)  # This function gets events for the user
        self.show_event_recommendations(events)

        # Log Out Button
        logout_button = tk.Button(self.root, text="Log Out", bg="#8a1538", fg="white",
                                  font=("Arial", 12), command=self.logout)
        logout_button.pack(pady=10)

    def get_personalized_events(self, username):
        # This method should fetch the user's event preferences from a database or recommendation model
        # For now, we return a static list of events (this can be dynamic based on the user)
        return [
            "Tech Conference 2025 - May 10th",
            "Music Festival 2025 - May 15th",
            "Art Exhibition - May 20th",
            "AI Workshop - May 22nd"
        ]

    def show_event_recommendations(self, events):
        events_label = tk.Label(self.root, text="Recommended Events for You:", font=("Arial", 14), bg="white")
        events_label.pack(pady=10)

        for event in events:
            event_label = tk.Label(self.root, text=event, font=("Arial", 12), bg="white")
            event_label.pack(pady=5)

    def logout(self):
        self.root.destroy()  # Close the homepage window
        from Login import LoginSystem  # Import LoginSystem from login_system.py
        login_window = tk.Tk()
        LoginSystem(login_window)  # Recreate the login window
        login_window.mainloop()

import tkinter as tk
from tkinter import messagebox


class Homepage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Personalized Event Recommendations")
        self.root.geometry("900x500")
        self.root.configure(bg="#e0f7fa")

        self.notifications = [
            "New event added: 'Robotics Fair 2025'",
            "Reminder: AI Workshop on May 22nd",
            "Update: Venue change for Music Festival"
        ]

        self.create_widgets()

    def create_widgets(self):
        # Top Banner
        top_frame = tk.Frame(self.root, bg="#039be5", height=80)
        top_frame.pack(fill="x", side="top")

        welcome_label = tk.Label(top_frame, text=f"Welcome, {self.username}!",
                                 font=("Arial", 18, "bold"), fg="white", bg="#039be5")
        welcome_label.place(x=20, y=20)

        # Search Bar
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(top_frame, textvariable=self.search_var, font=("Arial", 12), width=30)
        search_entry.place(x=400, y=26)

        search_btn = tk.Button(top_frame, text="Search", font=("Arial", 10, "bold"), bg="#0288d1", fg="white",
                               command=self.search_events)
        search_btn.place(x=680, y=25)

        # Side Panel
        side_panel = tk.Frame(self.root, bg="#b3e5fc", width=200)
        side_panel.pack(fill="y", side="left")

        profile_label = tk.Label(side_panel, text="👤 My Profile", font=("Arial", 14, "bold"),
                                 bg="#b3e5fc", fg="#01579b")
        profile_label.pack(pady=30)

        btn_events = tk.Button(side_panel, text="📅 Events", font=("Arial", 12), bg="#4fc3f7", fg="white",
                               width=18, relief="flat", command=self.show_events)
        btn_events.pack(pady=10)

        btn_notif = tk.Button(side_panel, text="🔔 Notifications", font=("Arial", 12), bg="#4fc3f7", fg="white",
                              width=18, relief="flat", command=self.show_notifications)
        btn_notif.pack(pady=10)

        btn_settings = tk.Button(side_panel, text="⚙️ Settings", font=("Arial", 12), bg="#4fc3f7", fg="white",
                                 width=18, relief="flat", command=self.show_settings)
        btn_settings.pack(pady=10)

        btn_logout = tk.Button(side_panel, text="🚪 Log Out", font=("Arial", 12), bg="#0288d1", fg="white",
                               width=18, relief="flat", command=self.logout)
        btn_logout.pack(pady=30)

        # Main Frame Container
        self.container = tk.Frame(self.root, bg="white")
        self.container.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Create Pages
        self.frames = {}
        for F in (self.EventsFrame, self.SettingsFrame, self.NotifFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("EventsFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_events(self):
        self.show_frame("EventsFrame")
        self.frames["EventsFrame"].update_events()

    def show_settings(self):
        self.show_frame("SettingsFrame")

    def show_notifications(self):
        self.show_frame("NotifFrame")

    def logout(self):
        self.root.destroy()
        from Login import LoginSystem
        login_window = tk.Tk()
        LoginSystem(login_window)
        login_window.mainloop()

    def search_events(self):
        query = self.search_var.get().lower().strip()
        self.frames["EventsFrame"].filter_events(query)
        self.show_events()

    def get_personalized_events(self, username):
        return [
            "Tech Conference 2025 - May 10th",
            "Music Festival 2025 - May 15th",
            "Art Exhibition - May 20th",
            "AI Workshop - May 22nd",
            "Robotics Fair 2025 - May 30th"
        ]

    # ---------- PAGES ----------
    class EventsFrame(tk.Frame):
        def __init__(self, parent, controller):
            super().__init__(parent, bg="white")
            self.controller = controller
            self.all_events = controller.get_personalized_events(controller.username)
            self.event_widgets = []

            self.label = tk.Label(self, text="🎉 Recommended Events for You:",
                                  font=("Arial", 14, "bold"), bg="white", fg="#039be5")
            self.label.pack(pady=20)

            self.events_container = tk.Frame(self, bg="white")
            self.events_container.pack()

            self.update_events()

        def update_events(self):
            self.display_events(self.all_events)

        def filter_events(self, query):
            filtered = [e for e in self.all_events if query in e.lower()]
            self.display_events(filtered)

        def display_events(self, events):
            for widget in self.events_container.winfo_children():
                widget.destroy()

            if not events:
                tk.Label(self.events_container, text="No events found.", font=("Arial", 12),
                         bg="white", fg="gray").pack()
            else:
                for event in events:
                    tk.Label(self.events_container, text=f"• {event}",
                             font=("Arial", 12), bg="white", anchor="w").pack(pady=3, padx=20, anchor="w")

    class SettingsFrame(tk.Frame):
        def __init__(self, parent, controller):
            super().__init__(parent, bg="white")
            label = tk.Label(self, text="⚙️ Settings", font=("Arial", 14, "bold"),
                             bg="white", fg="#039be5")
            label.pack(pady=20)

            sample_setting = tk.Label(self, text="(Settings content goes here)",
                                      font=("Arial", 12), bg="white")
            sample_setting.pack(pady=10)

    class NotifFrame(tk.Frame):
        def __init__(self, parent, controller):
            super().__init__(parent, bg="white")
            tk.Label(self, text="🔔 Notifications", font=("Arial", 14, "bold"),
                     bg="white", fg="#039be5").pack(pady=20)

            for note in controller.notifications:
                tk.Label(self, text=f"• {note}", font=("Arial", 12), bg="white",
                         anchor="w").pack(pady=3, padx=20, anchor="w")

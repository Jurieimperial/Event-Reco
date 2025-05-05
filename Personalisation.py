import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

class Personalisation:
    def __init__(self, root):
        self.tk_uploaded_image = None
        self.root = root
        self.root.title("Personalisation")
        self.root.geometry("1500x900")
        self.root.configure(bg="#add8e6")

        # Create the canvas
        self.canvas = tk.Canvas(self.root, width=1920, height=1080, bg="#add8e6", highlightthickness=0)
        self.canvas.place(x=80, y=100)

        # Header text
        self.canvas.create_text(600, 15, text="Personalisation", font=("Roboto", 30), fill="#373A40")

        # First rectangle
        self.create_rounded_rectangle(460, 50, 1360, 450, 30, fill="white", outline="", width=0)

        # Section labels in first rectangle
        self.canvas.create_text(629, 120, text="Personal Information", font=("Roboto", 18), fill="#61677A")
        self.canvas.create_text(640, 200, text="Password and Security", font=("Roboto", 18), fill="#61677A")
        self.canvas.create_text(650, 280, text="Accessibility and Display", font=("Roboto", 18), fill="#61677A")
        self.canvas.create_text(642, 360, text="Language and Regions", font=("Roboto", 18), fill="#61677A")

        # Second rectangle
        self.create_rounded_rectangle(460, 470, 1360, 746, 15, fill="white", outline="", width=0)
        self.canvas.create_text(560, 520, text="Themes", font=("Roboto", 18), fill="#61677A")

        # Theme palette circles
        colors = ["#FF5733", "#FF8D1A", "#FFC300", "#DAF7A6", "#33FFBD",
                  "#33D4FF", "#3385FF", "#A833FF", "#FF33A8", "#FF3333"]
        x_start = 560
        y_center = 580
        radius = 15
        spacing = 40

        for i, color in enumerate(colors):
            x = x_start + i * spacing
            self.canvas.create_oval(x - radius, y_center - radius, x + radius, y_center + radius,
                                    fill=color, outline="black")

        # Profile picture circle (300x300)
        self.circle = self.canvas.create_oval(0, 0, 300, 300, fill="white", outline="black")

        # Text under profile picture
        self.canvas.create_text(150, 320, text="@username | Organization | Bio", font=("Roboto", 12), fill="#61677A")

        # Load default camera icon
        self.default_image = Image.open("images/camera.png").resize((30, 30))
        self.tk_default_image = ImageTk.PhotoImage(self.default_image)

        # Camera button
        self.circle_button = self.canvas.create_oval(240, 240, 300, 300, fill="white", outline="black")
        self.button_icon = self.canvas.create_image(270, 270, image=self.tk_default_image)

        # Bind upload function
        self.canvas.tag_bind(self.circle_button, "<Button-1>", self.upload_image)
        self.canvas.tag_bind(self.button_icon, "<Button-1>", self.upload_image)

        # Add the third rectangle underneath the profile section
        self.create_rounded_rectangle(50, 350, 250, 650, 20, fill="white", outline="", width=0)

        # Add the dark blue "Homepage" button under the third rectangle
        self.home_button = tk.Button(self.root, text="Go To Homepage", font=("Roboto", 12),
                                     bg="#0D47A1", fg="white", relief="flat", cursor="hand2")
        self.home_button.place(x=155, y=800, width=150, height=30)

        self.uploaded_img_id = None

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        outline = kwargs.pop("outline", "")
        fill = kwargs.pop("fill", "")
        width = kwargs.pop("width", 0)

        self.canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius, outline=outline, fill=fill, width=width)
        self.canvas.create_oval(x2 - 2 * radius, y1, x2, y1 + 2 * radius, outline=outline, fill=fill, width=width)
        self.canvas.create_oval(x1, y2 - 2 * radius, x1 + 2 * radius, y2, outline=outline, fill=fill, width=width)
        self.canvas.create_oval(x2 - 2 * radius, y2 - 2 * radius, x2, y2, outline=outline, fill=fill, width=width)

        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, outline=outline, fill=fill, width=width)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, outline=outline, fill=fill, width=width)

    def upload_image(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            image = Image.open(file_path).resize((300, 300)).convert("RGBA")

            mask = Image.new('L', (300, 300), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 300, 300), fill=255)
            image.putalpha(mask)

            self.tk_uploaded_image = ImageTk.PhotoImage(image)

            if self.uploaded_img_id:
                self.canvas.itemconfig(self.uploaded_img_id, image=self.tk_uploaded_image)
            else:
                self.uploaded_img_id = self.canvas.create_image(150, 150, image=self.tk_uploaded_image)

            self.canvas.tag_raise(self.circle_button)
            self.canvas.tag_raise(self.button_icon)

if __name__ == "__main__":
    personalisation_window = tk.Tk()
    app = Personalisation(personalisation_window)
    personalisation_window.mainloop()

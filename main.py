import tkinter as tk
from PIL import Image, ImageTk

class ImageModel:
    def __init__(self, initial_size, max_size, step):
        self.initial_size = initial_size
        self.max_size = max_size
        self.step = step
        self.current_size = initial_size
        self.increasing = True

    def update_size(self):
        if self.increasing:
            self.current_size += self.step
            if self.current_size >= self.max_size:
                self.current_size = self.max_size
                self.increasing = False
        else:
            self.current_size -= self.step
            if self.current_size <= self.initial_size:
                self.current_size = self.initial_size
                self.increasing = True

class ImageView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.label = tk.Label(root)
        self.label.pack()

    def display_image(self, image):
        self.label.config(image=image)
        self.label.image = image

class ImageController:
    def __init__(self, root, model, view, image_path):
        self.model = model
        self.view = view
        self.root = root
        self.image_path = image_path

        self.root.bind("<Button-1>", self.on_click)
        self.update_image()

    def update_image(self):
        img = Image.open(self.image_path)
        img = img.resize((self.model.current_size, self.model.current_size), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(img)
        self.view.display_image(self.tk_image)

    def on_click(self, event):
        self.model.update_size()
        self.update_image()

if __name__ == "__main__":
    # Параметри
    initial_size = 100
    max_size = 200
    step = 20
    image_path = "C:/Users/09990.DESKTOP-QEMSV0C/OneDrive/Зображення/Saved Pictures/IMG_4185.jpg"

    root = tk.Tk()
    root.title("Image Resizer")

    model = ImageModel(initial_size, max_size, step)
    view = ImageView(root, None)
    controller = ImageController(root, model, view, image_path)

    root.mainloop()

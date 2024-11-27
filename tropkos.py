import tkinter as tk
from tkinter import messagebox

class CandyDispenser:
    def __init__(self):
        self.stack = []
        self.max_size = 9
        self.colors = ['#FF5733', '#33FF57', '#3357FF', '#FFC300']  # Bright and contrasting colors

    def push(self, candy_color):
        if self.size() < self.max_size:
            self.stack.append(candy_color)
        else:
            raise OverflowError("CANDY DISPENSER is FULL!")

    def pop(self):
        if self.is_empty():
            raise IndexError("The CANDY DISPENSER is out of CANDY")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class CandyDispenserGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dispenser = CandyDispenser()
        self.title("Peremende Candy Dispenser")
        
        self.geometry("500x500")
        self.canvas = tk.Canvas(self, width=200, height=350, bg="#F0F8FF")  # Alice blue background for a fresh look
        self.canvas.pack(pady=10)

        # Enhanced button styles
        self.push_button = tk.Button(self, text="Refill Candy", command=self.push_candy, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.push_button.pack(pady=5)

        self.pop_button = tk.Button(self, text="Dispense Candy", command=self.pop_candy, bg="#F44336", fg="white", font=("Arial", 12, "bold"))
        self.pop_button.pack(pady=5)

        self.display_button = tk.Button(self, text="Candy Count", command=self.display_size, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.display_button.pack(pady=5)

    def push_candy(self):
        if self.dispenser.size() < self.dispenser.max_size:
            color = self.dispenser.colors[self.dispenser.size() % len(self.dispenser.colors)]
            self.dispenser.push(color)
            self.animate_candies()
        else:
            messagebox.showerror("Error", "CANDY DISPENSER is FULL! Cannot add more CANDY.")

    def pop_candy(self):
        try:
            self.dispenser.pop()
            self.animate_candies()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def display_size(self):
        size = self.dispenser.size()
        messagebox.showinfo("Candy Count", f"There are {size} candies in the dispenser.")

    def animate_candies(self):
        self.canvas.delete("all")
        size = self.dispenser.size()
        
        # Compute heights based on the number of candies
        candy_height = 350 / max(size, 1)  # Prevent division by zero

        # Create candies to appear at the bottom before animating
        for i in range(size):
            candy_color = self.dispenser.stack[i]
            initial_y_position = 350  # start from the bottom
            candy = self.canvas.create_rectangle(
                50, initial_y_position, 150, initial_y_position - candy_height,
                fill=candy_color, outline="black", width=2, tags=f"candy{i}"
            )
            self.animate_single_candy(candy, 350 - (i * candy_height))

    def animate_single_candy(self, candy, target_y):
        current_position = 350  # Start from the bottom
        steps = 20  # Number of steps to reach the final position
        delta = (target_y - current_position) / steps  # Calculate the distance to move each step

        for step in range(steps):
            self.after(step * 30, lambda pos=candy, dp=delta: self.move_candy(pos, dp))

    def move_candy(self, candy, delta):
        self.canvas.move(candy, 0, delta)
        self.canvas.update()  # Update the canvas after moving

if __name__ == "__main__":
    app = CandyDispenserGUI()
    app.mainloop()
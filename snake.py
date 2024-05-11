import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.direction = "LEFT"
        self.food = self.create_food()
        self.score = 0

        self.draw_snake()
        self.draw_food()

        self.master.bind("<KeyPress>", self.change_direction)
        self.move()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tag="snake")

    def draw_food(self):
        self.canvas.delete("food")
        self.food = self.create_food()
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red", tag="food")

    def create_food(self):
        x = random.randrange(0, 400, 10)
        y = random.randrange(0, 400, 10)
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif key == "Right" and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif key == "Up" and self.direction != "DOWN":
            self.direction = "UP"
        elif key == "Down" and self.direction != "UP":
            self.direction = "DOWN"

    def move(self):
        head = self.snake[0]
        if self.direction == "LEFT":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + 10, head[1])
        elif self.direction == "UP":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 10)

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 10
            self.draw_food()
        else:
            self.snake.pop()

        if (new_head[0] < 0 or new_head[0] >= 400 or
            new_head[1] < 0 or new_head[1] >= 400 or
            new_head in self.snake[1:]):
            self.game_over()
            return

        self.draw_snake()
        self.master.after(100, self.move)

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over\nScore: {}".format(self.score), fill="white", font=("Arial", 20))
        restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        restart_button.pack()

    def restart_game(self):
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.direction = "LEFT"
        self.score = 0
        self.canvas.delete("all")
        self.canvas.pack()
        self.draw_snake()
        self.draw_food()
        self.master.bind("<KeyPress>", self.change_direction)
        self.move()

def main():
    root = tk.Tk()
    app = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

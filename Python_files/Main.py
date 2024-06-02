import tkinter as tk
from tkinter import simpledialog
import csv
headings = ["Title", "Genre", "Publisher", "Release.Console", "Release.Year"]
class Table(tk.Frame):
    def __init__(self, parent, data):
        rows = len(data)
        columns = len(data[0]) if data else 0

        tk.Frame.__init__(self, parent)

        # Create a canvas and add a scrollbar to it
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Bind the scrollable frame's yview to the canvas's yview
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create table headings
        self.labels = [[None] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                self.labels[i][j] = tk.Label(self.scrollable_frame, text=data[i][j], borderwidth=1, relief="solid", width=25, height=2)
                self.labels[i][j].grid(row=i, column=j, sticky="nsew")

        # Adjust row and column weights to make them expandable
        for i in range(rows):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
            
def button_1():
    button = 0
    display_input_box(button)
    

def button_2():
    button = 1
    display_input_box(button)
    

def button_3():
    button = 2
    display_input_box(button)
    


def button_4():
    button = 3
    display_input_box(button)
    


def button_5():
    button = 4
    display_input_box(button)
    


def button_6():
    button = 5
    display_input_box(button)
    

    
def display_input_box(button):
    user_input = simpledialog.askstring("Input", "Enter something:")
    if user_input is not None:
        CSV_read(button,user_input)
        
def CSV_read (search_param,user_request):
    user_request = user_request.lower()
    data = []
    
    with open('Video_game_project.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        if search_param == 5:
            for row in csv_reader:
                if any (user_request in cell.lower() for cell in row):
                    data.append(row)
        else:
            for row in csv_reader:
                if user_request in row[search_param].lower():
                    data.append(row)
    for widget in root.winfo_children():
        if isinstance(widget, Table):
            widget.destroy()
    table = Table(root,data)
    table.pack(expand=True, fill ="both")        

# Create the main window
root = tk.Tk()
root.geometry("920x600")
root.title("Button GUI")

header = tk.Label(root, text="Video game search", font=("Helvetica", 16))
header.pack(pady=10)  # Add some padding around the header

# Create and place buttons in the window
btn1 = tk.Button(root, text="Title", command=button_1)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Genre", command=button_2)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Publisher", command=button_3)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Console", command=button_4)
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Release year", command=button_5)
btn5.pack(pady=5)

btn6 = tk.Button(root, text="All", command=button_6)
btn6.pack(pady=5)

# Run the main event loop
root.mainloop()


        
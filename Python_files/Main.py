import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import requests
def button_1():
    button = "" 
    display_input_box(button)

def button_2():
    button = "publishers"
    display_input_box(button) 
    
def button_3():
    button = "dates"
    display_input_box(button)    
      
def display_input_box(button):
    user_input = simpledialog.askstring("Input", "Enter something:")
    if user_input is not None:
        API_read(user_input,button)
        

def API_read(user_request,button):
    user_request = user_request.lower()
    data = []
    headers = {
        "X-RapidAPI-Key": "1220e8bca4msh0ae96f8e29fe247p1cc760jsn74cf7b671963",
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
    }
    
    #requires search by ID
    if button == "publishers":
        url = f"https://rawg-video-games-database.p.rapidapi.com/games?key=ffbe944544e84b7bba0c133b3ac90b0f&publishers={user_request}&page_size=25"

    elif button == "dates":
        url = f"https://rawg-video-games-database.p.rapidapi.com/games?key=ffbe944544e84b7bba0c133b3ac90b0f&dates={user_request}&page_size=25"
    else:
        url = f"https://rawg-video-games-database.p.rapidapi.com/games?key=ffbe944544e84b7bba0c133b3ac90b0f&search={user_request}&page_size=25" 
    
    response = requests.get(url, headers=headers)
    games_data = response.json()
    total_pages = games_data.get('page_count', 0)
    print(total_pages)
    for i in range(0, total_pages + 1):
        response = requests.get(url, headers=headers)

            # Convert the response to JSON
        json_data = response.json()

            # Get the list of games from the JSON data
        games = json_data.get('results', [])

       
        for game in games:
                # Create a list of values in the correct order
            row_list = [game.get('name', ''), game.get('released', ''), game.get('rating', '')]

            if any(user_request in str(value).lower() for value in row_list):
                data.append(row_list)

            # Get the URL for the next page of results
        url = json_data.get('next')

    # Clear existing widgets
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=('Name', 'Released', 'Rating'), show='headings')
    
    # Set the column headings
    tree.heading('Name', text='Name')
    tree.heading('Released', text='Released')
    tree.heading('Rating', text='Rating')

    # Add the data to the Treeview widget
    for row in data:
        tree.insert('', 'end', values=row)

    tree.pack() 

# Create the main window
root = tk.Tk()
root.geometry("920x600")
root.title("Button GUI")

header = tk.Label(root, text="Video game search", font=("Helvetica", 16))
header.pack(pady=10)  # Add some padding around the header

# Create and place buttons in the window
btn1 = tk.Button(root, text="Search by Name", command=button_1)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Search by Publishers", command=button_2)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Search by release date", command=button_3)
btn3.pack(pady=5)
# Run the main event loop
root.mainloop()


        
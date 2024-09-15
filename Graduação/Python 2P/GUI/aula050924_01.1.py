import tkinter as tk

def add_username():
    username = entry.get()  # Get the username from the Entry widget
    if username:
        listbox.insert(tk.END, username)  # Add the username to the Listbox
        entry.delete(0, tk.END)  # Clear the Entry field

def on_select(event):
    # Get the index of the clicked item
    selected_index = listbox.curselection()
    if selected_index:
        # Get the value of the selected item
        selected_username = listbox.get(selected_index)
        print(f"Selected username: {selected_username}")  # Print to the console

def list_usernames():
    # Create the main window
    root = tk.Tk()
    root.title("User List")

    # Create a Listbox widget
    global listbox
    listbox = tk.Listbox(root, width=50, height=10)
    listbox.pack(pady=20)

    # Bind the Listbox selection event to the 'on_select' function
    listbox.bind('<<ListboxSelect>>', on_select)

    # Create an Entry widget for user input
    global entry
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    # Create a Button to add usernames to the Listbox
    add_button = tk.Button(root, text="Add Username", command=add_username)
    add_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

# Call the function to display the list of usernames
list_usernames()
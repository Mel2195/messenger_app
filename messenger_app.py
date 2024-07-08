import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mel" and password == "1121":
        # Clear the screen
        for widget in root.winfo_children():
            widget.destroy()
        # Create messenger interface
        create_messenger_interface()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

def create_messenger_interface():
    # Title
    title_label = tk.Label(root, text="Messenger", font=("Helvetica", 24, "bold"), pady=10)
    title_label.pack()

    # Scrollable section for messages
    messages_frame = tk.Frame(root)
    messages_frame.pack(pady=10)

    messages_scrollbar = tk.Scrollbar(messages_frame)
    messages_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    messages_listbox = tk.Listbox(messages_frame, yscrollcommand=messages_scrollbar.set, height=15, width=50, font=("Helvetica", 12))
    messages_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    messages_scrollbar.config(command=messages_listbox.yview)

    # Text field for inputting a message
    message_entry = tk.Entry(root, width=30, font=("Helvetica", 20))
    message_entry.pack(padx=10, pady=5, fill="x", side=tk.LEFT)

    # Send button
    send_button = tk.Button(root, text="Send", command=lambda: send_message(message_entry.get(), messages_listbox), font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="purple")
    send_button.pack(padx=10, pady=5, fill="x", side=tk.RIGHT)

    # Logout button
    logout_button = tk.Button(root, text="Logout", command=logout, font=("Helvetica", 12), fg="purple")
    logout_button.place(relx=1, rely=0, anchor="ne")

def send_message(message, messages_listbox):
    # Placeholder function for sending messages
    messages_listbox.insert(tk.END, message)

def logout():
    # Clear the screen
    for widget in root.winfo_children():
        widget.destroy()
    # Recreate the login page
    create_login_page()

def create_login_page():
    global password_entry, username_entry

    # Username and Password labels and entry fields
    username_label = tk.Label(root, text="Username:", font=("Helvetica", 14))
    username_label.pack(pady=5)

    username_entry = tk.Entry(root, font=("Helvetica", 14))
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:", font=("Helvetica", 14))
    password_label.pack(pady=5)

    password_entry = tk.Entry(root, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=5)

    # Login button
    login_button = tk.Button(root, text="Login", command=login, font=("Helvetica", 14, "bold"), fg="purple")
    login_button.pack(pady=10)

# Main program
root = tk.Tk()
root.title("Messenger Login")
root.geometry("800x500")
root.resizable(False, False)  # Make the window non-resizable

# Initial creation of the login page
create_login_page()

root.mainloop()

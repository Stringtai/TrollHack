import time
import webbrowser
import tkinter as tk

# List of messages to display in the GUI
texts = ["Hacking in progress", "Access granted", "Trojan horse deployed", "System breached", "Encrypting data", "Copying Files", "completed"]
index = 0

# Ask user for name and age
Name = input("what is your name?")
Age = input("what is your age?")

# Check if user is 16 years old and name matches specific values
if int(Age) == 16 and (Name == "String" or Name == "string"):
    time.sleep(1)
    Password = input("what is the password?")
    
    # Check if password is correct
    if int(Password) == 222:
        print("Hello boss")
        time.sleep(1)
        print("starting COS programs")
        
        # Function to update GUI text periodically
        def change_text():
            global index
            label.config(text=texts[index])
            
            # Open a website when the last message is displayed
            if texts[index] == "completed":
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                root.destroy()
            else:
                index = (index + 1) % len(texts)
            root.after(2000, change_text)
        
        # Initialize Tkinter window
        root = tk.Tk()
        root.title("If you are reading this you are gay")
        root.geometry("400x200")
        root.configure(bg='black')

        # Create and configure label
        label = tk.Label(root, text="Hacking in progress", font=("Helvetica", 20), fg='green', bg='black')
        label.pack(pady=20)

        # Start text change function
        change_text()

        # Run the Tkinter event loop
        root.mainloop()
        
        print("opening website")
        time.sleep(0.2)
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
else:
    # If authentication fails, display fake hacking messages and open prank website
    print("you are not allowed")
    time.sleep(1)
    print("Opening remote IP grabber")
    time.sleep(3)
    print("Sending IP to Remote Access Programs")
    time.sleep(4)
    webbrowser.open("https://youareanidiot.cc")

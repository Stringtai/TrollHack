import time
import webbrowser
import tkinter as tk

texts = ["Hacking in progress", "Access granted", "Trojan horse deployed","System breached", "Encrypting data", "Copying Files", "completed"]
index = 0

Name = input("what is your name?")
Age = input("what is your age?")
if int(Age) == 16 and (Name == "String" or Name == "string"):
    time.sleep(1)
    Password = input("what is the password?")
    if int(Password) == 222:
        print("Hello boss")
        time.sleep(1)
        print("starting COS programs")
        def change_text():
            global index
            label.config(text=texts[index])
            if texts[index] == "completed":
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                root.destroy()
            else:
                index = (index + 1) % len(texts)
            root.after(2000, change_text)
        root = tk.Tk()
        root.title("If you are reading this you are gay")
        root.geometry("400x200")
        root.configure(bg='black')

        label = tk.Label(root, text="Hacking in progress", font=("Helvetica", 20), fg='green', bg='black')
        label.pack(pady=20)

        change_text()

        root.mainloop()
        print("opening website")
        time.sleep(0.2)
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
else:
    print("you are not allowed")
    time.sleep(1)
    print("Opening remote IP grabber")
    time.sleep(3)
    print("Sending IP to Remote Acess Programs")
    time.sleep(4)
    webbrowser.open("https://youareanidiot.cc")



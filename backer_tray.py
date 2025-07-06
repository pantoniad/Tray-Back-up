import pystray
import PIL.Image
import subprocess
import tkinter as tk
from tkinter import filedialog
import os
import sys
import threading

### --------------------- Functions --------------------- ###

def ask_directory(title):
    """
    ask_directory (function): this function is responsible for collecting the source and
                              destination paths.
    
    Inputs:
    - title: the title used for the askdirectory method, str

    Outputs:
    - path: the source/destination path selected, str
    """
    # Create the object
    root = tk.Tk()
    root.withdraw() 
    root.attributes("-topmost", True)

    # Ask for the path
    path = filedialog.askdirectory(initialdir= "C:/", title=title)
    
    # Cleanly destroy the hidden root window
    root.destroy()  
    return path

def resource_path(relative_path):
    """
    resource_path: gets the absolute path to the resource needed

    Inputs:
    - relative_path: the relative path of the resource, str

    Outputs:
    - absolute path: the absolute path of the resource, str
    
    """

    # Get tha absolute path from the temporary unpacked directory
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    
    # Construct the absolute path
    absolute_path = os.path.join(os.path.abspath("."), relative_path)
    return absolute_path

# Create trigger function 
def clicked(icon, item):
    """
    clicked: a function that is responsible for what happens when the user
             interacts with the icon on the tray. Threading is used to make 
             use of the tkinter askdirectory method

    Inputs:
    - icon: the pystray icon instance,
    - item: the item presented to the user as a selection option

    Outputs:
    - None: working properly, this function should copy the files from the 
            source to the destination folder
    """
    # Use threading
    if str(item) == "Backup data?":
        threading.Thread(target=backup_sequence).start()

    # Terminate the tray app
    elif str(item) == "Exit":
        icon.stop()

def backup_sequence():
    """
    backup_sequence: a function used along side clicked acting as a main thread
                     for the ask_directory function. askdirectory method of the 
                     tkinter library needs to run on the main thread

    Inputs:
    - None

    Outputs:
    - None: working properly, this function should copy the files from the 
            source to the destination folder
    """

    # Get source path
    source = ask_directory("Select source folder")
    if not source:
        print("No source selected.")
        return

    # Get destination path
    destination = ask_directory("Select destination folder")
    if not destination:
        print("No destination selected.")
        return
    
    # User confirmation
    if not confirm_copy(source, destination):
        print("User cancelled backup.")
        return

    # Flags used for the subprocess
    flags = ["/e", "/mt"]
    ans = subprocess.call(["robocopy", source, destination] + flags)

    # Subprocess return code check. For code info check robocopy documentation
    if ans < 8:
        print("Backup completed. Code returned: ", ans)
    else:
        print("Backup failed with code:", ans)

def confirm_copy(source, destination):
    """
    confirm_copy: a fucntion that generates a prompt to confirm the paths specified and
                  give a go/no-go for the copying

    Inputs:
    - source: source path, str,
    - destination: destination path, str

    Outputs:
    - decision["answer"]: a dictionary containg a "True" of "False" statement, dictionary
    """
    decision = {"answer": None}

    def on_yes():
        decision["answer"] = True
        window.destroy()

    def on_no():
        decision["answer"] = False
        window.destroy()

    window = tk.Tk()
    window.title("Confirm Backup")
    window.geometry("400x250")
    window.attributes("-topmost", True)

    tk.Label(window, text="Backup Confirmation", font=("Segoe UI", 12, "bold")).pack(pady=10)

    tk.Label(window, text="Source Folder:", font=("Segoe UI", 10, "underline")).pack()
    tk.Label(window, text=source, wraplength=380).pack(pady=5)

    tk.Label(window, text="Destination Folder:", font=("Segoe UI", 10, "underline")).pack()
    tk.Label(window, text=destination, wraplength=380).pack(pady=5)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=15)

    tk.Button(button_frame, text="Yes", width=10, command=on_yes).pack(side="left", padx=10)
    tk.Button(button_frame, text="No", width=10, command=on_no).pack(side="right", padx=10)

    window.mainloop()
    return decision["answer"]

### --------------------- Execution --------------------- ###

# Call image path for the icon
image_path = resource_path(r"C:\GitHub\Tray-Back-up\usb_arrow.png")
image = PIL.Image.open(image_path)

# Create icon object
icon = pystray.Icon("BackUp", image, menu = pystray.Menu(
    pystray.MenuItem("Backup data?", clicked),
    pystray.MenuItem("Exit", clicked)
))

# Run tray app
icon.run()
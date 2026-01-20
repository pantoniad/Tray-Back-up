### Manual on the usage of the BackerApp

This is a simple manual on how to use the application. It includes:
1. What the different functions of the application are, and
2. How to create the executable file using pyinstaller

#### Features of the application

The app is used to copy large amounts of data from one folder to another
and is especially well suited for iterative back-up functions. Using the 
robocopy tool, it can transfer large amounts of data from one directory to 
another. Using the tool's delta function, it is able to only transfer the 
changes from one update to the next, when dealing with the same destination
folder again and again. 

To use the app, you follow the next steps:
1. Run the executable (located in the dist folder)
2. On the windows tray, on the bottom right corner of the window, right-click
the usb icon.
3. By clicking the "Back-up?" menu-item, you are greeted with a screen to select
the source folder. After selecting, the destination folder needs to be chosen and,
lastly, a pop-up window is given to make sure of the source and destination 
folders. By selecting "continue" the copying process starts. 
4. By clicking "Exit" the application is terminated and by clicking "Information" the
user is transfered to the GitHub page of the repository. 

If the user terminates the process through one of the file explorer windows, then the 
app remains active in the tray. The app is terminated only by selecting the "Exit" 
menu item. 

#### How to create the executable

There are two ways to create the executable, based on the guidelines given in the 
pyinstaller web-manual:
1. To create an executable + a corresponding folder, and
2. To create a standalone executable file

In the first case, anything needed for the application is packed inside a folder 
called "_internal" and placed alongside the executable file inside the "dist" folder. 

In the second case, only the executable file is generated. 

For the interested user, I suggest reading the manual of the pyinstaller, directly, 
to better understand how the bundling process works. 

For the first case, the user can run the next command in the windows CMD
- pyinstaller --add-data "Resources/usb_arrow.png;." backer_tray.py

If the spec file has been altered manually, then the following line should be used
instead:
- pyinstaller backer_tray.spec

For the second case:
- pyinstaller --onefile --windowed "Resources/usb_arrow.png;." backer_tray.py
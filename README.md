# Tray-Back-up
A file back-up application that lets you copy whole folders from one place of your storage to another. 
This application uses "robocopy" with multithreading to copy your files easily and at very high speeds.

Some basic considerations:
- This repository contains both the code for the app ("backer_tray.py") and a .exe file placed inside the dist folder. One can either use the code and make changes/enhancments to the app, or use the .exe application.
- For it to work you need to have the "usb_arrow.png" image file in the same directory as all the other files. As path specified in the code is "C:\GitHub\Tray-Back-up\usb_arrow.png" it would be best to keep this folder structure as is. A fix might be coming later on

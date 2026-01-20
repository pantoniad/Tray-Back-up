Application requirements:
- Tool that copies the contents of a folder to a new directory in the disk,
- The process should be equally as fast, or even faster, than drag and drop,
- Folder created should be compressed,
- Folder should be named after the current datetime,
- Should be a standalone application that works on the tray of windows,
- Should be able to work on any windows system

Current problems:
-[x] File cannot be used in other windows systems: How do we solve that? How does the PyInstaller handle directories?
-[x] Robocopy needs to be checked again to only include either added or changed files, not deleted one (done)
-[] Add the option for the user to include a whole save of the current source folder in a separate directory.

Additional suggestions:
-[] Compose a manual on how to use and compile the app,
-[x] Reorganize some stuff (never ending task...)
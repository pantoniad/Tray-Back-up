### Notes on the "Robocopy" method and other methods that can establish the back-up function

Robocopy is a process that "will only copy a file if the source and destination have different time stamps or different file sizes". 
This means that robocopy creates a "stamp" file that keeps tracks of what files change over-time, or between saves. 

So, based on the below links and the research that ChatGPT conducted, the robocopy function is a command-line replication tool that specializes in large-directory trees and is advised to be used on unreliable disks or networks. It also enables high performance copying through a multi-thread function. 

Its main advantage, against other similar command-line tools, is that it keeps a record of the directory structrue and checks what files have been changed. Based on the set of options given, it copies or rejects the corresponding files, excluding unchanged or changed files.

Sources:
1. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy
2. https://ss64.com/nt/robocopy.html

Conclusion:
- Based on the above, robocopy was not used correctly up until now: Only the copying function was used and not all the other functions provided by the tool (synchronization),
- The above must have been the reaon that the tool was slow
- It can be used as is, meaning that only some modifications need to be made on the core functions that hanlde the "robocopy" tool and can be expanded further to included most of the options available,

The question now that arises:
- Do we need to keep a full copy of the current version? Or do we just want to update the same folder again and again?
- In the first option, any older option can be accessed, regardless. But with the second option, only the most up-to-date copy can be accessed.
- As a solution to this, an option could be given to the user for a full copy of the current back-up could be saved along-side the updated folder. This, though, would greatly increase the required time.

#### Research on alternatives

Windows alternatives:
- FastCopy: native on Windows and also comes with a GUI, closed source though but crazy fast. Has most of the features that robocopy offers,
- TeraCopy: similar to FastCopy, comes with a GUI, and can be coupled with shell commands,


#### Baseline conclusion on what approach to use for the copying procedure
- Robocopy offers a very good and consice approach. 
- Houses all of the features required and is native to windows,
- This means, though, that an extension to MAC might not be possible

#### Execution
Currently: The source directory is copied anew, every time the back-up process is initiated. This means that the process is slow and the delta-type file created is not used.
Goal: 
- make the robocopy command keep only the files that have been altered or added. Do not kep the deleted ones in the destination folder. 
- The destination folder is, also, not created anew but the same one is used. This allows for the delta-type system to be included.
- Addition: if the user want to create a full, separate copy, of the source folder, they should be allowed to. 

### How to make the software able to work on multiple windows systems

#### Basics of PyInstaller

PyInstaller is tool used to bundle a python application, and all its dependencies, into a single package that can later be accessed, intependently, by any other user. The bunlde can either be a folder or a single file. By default, PyIntaller, keeps an instance of the current python bootloader and also all the corresponding dependencies. The application does not require the use of any python instance in the recieving user's system. 

Run to generate a folder:               pyinstaller myscript.py
Run to generate a windowed appliation:  pyinstaller --onefile --windowed myscript.py
The above must be run on the **command line**.

In the case of bundling the application in the form of a **folder**, the resulting bundle an be compressed and sent to a different user. In the case that any code is altered in the application, then the same procedure can be followed, but only the executable file needs to be distributed. 

In the case of distributing a **single file programm** the application is packages in a sinlge executable file. Whenever the user opens the file, a temporary folder is created in the temp-fodler location of the OS. The folder is deleted, after the application is terminated but this is not the case if the app crashes or is forced to stop. The temporary folder location can be controlled. Do not give administrator priviliges to the application.

#### Using PyInstaller

Command: pyinstaller [options] script [script...] | specfile

The work flow can be described as below, after analysing the script:
- Creates a .spec file in the same directory as the script,
- Creates a build folder in the same directory, if it does not exist,
- Creates a series of log files,
- Creates a dist folder, in the same directory, if it does not exist,
- Creates the executable file

List of options:
1. -h or --help: show help message,
2. -v or --version: show program version
3. --distpath: destination path (dist)
4. --workpath WORKPATH: where to put the temporary path
5. --clean: clean pyinstaller cache before building
6. --log-level LEVEL: level of detail in the logs (see pyinstaller webpage for various levels)


What to generate:
1. -D: one-folder bundle,
2. -F: one-file bundle,
3. --specpath DIR: folder for the spec file,
4. -n, --name NAME: name to be given to the bundled app,

#### Using PyInstaller
As the size of the execution command can be quite long, one can either use a BAT file (windows), in case they use the command line for the development, or the "run" method from the PyInstaller.__main___ package. 


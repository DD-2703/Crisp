""""
Main file.
"""
import sys
from functions import download, search, show_all

if len(sys.argv) == 1:
    print("""\nWelcome to Fig Crisp.  
~About Crisp~
Crisp is a package manager (aimed towards developers) that lets you download many applications, hassle-free, right 
through the command-line.\n"""
          )
    print("""Usage: 
        crisp download [application name]       download an application
        crisp search [application name]         search for an application in the app-list
        crisp list                              list all the applications in the app-list    

        Note: Make sure to append '-32bit' after every application name, without spaces, if you want to install the 32bit version of the program, if any.
              However, for programs that only support 64bit version, this cannot be done, but for those who only support 32bit, no need of adding the tag. 
    """)

else:
    if len(sys.argv) == 3:
        if sys.argv[1] == "download":
            download(sys.argv[2])
        elif sys.argv[1] == "search":
            search(sys.argv[2])
    elif len(sys.argv) == 2:
        if sys.argv[1] == "list":
            show_all()

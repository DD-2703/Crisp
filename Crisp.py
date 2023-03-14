""""
Main file. Handles all functions when crisp is passed wth various arguments.
"""

import sys
from functions import download, download32, search, show_all
import exceptions as exp

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
        crisp download32 [application name]     does the same work as the download command, but for 32 bit packages
        
        32 bit application downloads are not implemented yet.
    """)

else:

    if len(sys.argv) == 3:

        if sys.argv[1] == "download":
            download(sys.argv[2])

        elif sys.argv[1] == "search":
            search(sys.argv[2])

        elif sys.argv[1] == "download32":
            download32()

        else:
            raise exp.CrispUnknownCommandError(f"Not found command {sys.argv[1]}")

    elif len(sys.argv) == 2:
        if sys.argv[1] == "list":
            show_all()

    else:
        raise exp.CrispUnknownCommandError(
            f"Could not find command {sys.argv[1]}. Run crisp without any arguments to get the documentation."
        )

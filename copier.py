#!/usr/bin/env python3

from sys import argv, exit
import os
import shutil
from time import sleep


try:
    # Check if the user has provided the correct number of arguments
    if len(argv) != 4:
        print("Usage: python3 index.py <structure> <destination> <source>")
        exit(1)

    # Get the path provided by the user
    STRUCTUREPATH = argv[1]
    STRUCTURE = os.walk(argv[1])

    # Get the new path provided by the user
    NEWPATH = argv[2]

    # Get the directory name provided by the user
    DIRPATH = argv[3]

    

    # Check if the path provided is a directory
    if os.path.isdir(STRUCTUREPATH) is False or os.path.exists(STRUCTUREPATH) is False:
        print("The path provided is not a directory")
        exit(1)

    # Check if the new path provided is a directory
    if os.path.isdir(NEWPATH) is False or os.path.exists(NEWPATH) is False:
        print("The path provided is not a directory")
        exit(1)

    # Check if the directory name provided is a directory
    if os.path.isdir(DIRPATH) is False or os.path.exists(DIRPATH) is False:
        print("The directory name provided is not a directory")
        exit(1)


    # remove .fdmdownload from any file extension
    for root, dirs, files in os.walk(STRUCTUREPATH):
        for file in files:
            if file.endswith(".fdmdownload"):
                os.rename(os.path.join(root, file), os.path.join(root, file[:-12]))
    

    # Create the directory if it doesn't exist
    for root, dirs, files in os.walk(DIRPATH):
        # Perform operations within this directory
        for structure_root, structure_dirs, structure_files in os.walk(STRUCTUREPATH):
            for temp_file in structure_files:
                if temp_file in files:
                    source = os.path.join(root, temp_file)
                    # create dir 
                    destination = structure_root.replace(STRUCTUREPATH, NEWPATH)
                    
                    os.makedirs(destination, exist_ok=True)
                    print("from: " + source)
                    print("to: " + destination)
                    print("copying this may take a while...")

                    try:
                        shutil.move(source, destination)
                    except shutil.Error:
                        print("File already exists")
                        pass
                    except OSError:
                        print("File already exists")
                        pass
                    except FileNotFoundError:
                        pass
                                
      
except KeyboardInterrupt:
    print("Exiting...")
    exit(0)
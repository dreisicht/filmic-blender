import os
# renames all files, folders and subfolders of the current working directory
# so that there are no spaces in the names
root = os.getcwd()
for path, subdirs, files in os.walk(root):
    for foldername in subdirs:
        print(foldername)
        newfoldername = foldername.replace(" ", "_")
        olddirectory = os.path.join(path, foldername)
        newdirectory = os.path.join(path, newfoldername)
        os.rename(olddirectory, newdirectory)
    for filename in files:
        print(filename)
        newfilename = filename.replace(" ", "_")
        oldfile = os.path.join(path, filename)
        newfile = os.path.join(path, newfilename)
        os.rename(oldfile, newfile)

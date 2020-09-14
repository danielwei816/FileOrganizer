from PIL import Image
import os, os.path


"""
path: the base path
extensions: the list of extensions to be sorted
folder: the name of the target folder
"""
def organize(path, extensions, folder):
    files = []
 
    # finds all files in the base path that possess one of the extensions in extensions and appends it to the list of files
    for file in os.listdir(path): # lists all files + directories in specified directory
        ext = os.path.splitext(file)[1] # splits directory name into [root, ext]
        if ext.lower() in extensions:
            files.append(file)

    if not folder in os.listdir(path): os.mkdir(os.path.join(path, folder))
    
    for file in files:
        suffixNum = 1
        duplicateFile = file
        while duplicateFile in os.listdir(os.path.join(path, folder)):
        # looking for a duplicate file
            duplicateFile = file + " (" + str(suffixNum) + ")"
            suffixNum += 1
            
        os.rename(os.path.join(path, file), os.path.join(os.path.join(path, folder), duplicateFile))
        

base_path = "/Users/daniel/"
folders = ["Desktop", "Downloads"]
visual_extensions = [".jpg", ".jpeg", ".png", ".raw" ".gif", ".mp4", ".mov", ".wmv", ".avi", ".flv"]
doc_extensions = [".pdf", ".doc", ".docx", ".txt", ".rtf", ".html", ".ppt", ".pptx", ".xls", "xlsx"]
media_types = [(visual_extensions, "Photos:Videos"), (doc_extensions, "Documents")]

for folder in folders:
    for media in media_types:
        organize(os.path.join(base_path, folder), media[0], media[1])

from PIL import Image
import os, os.path

def organize(path, extensions, folder):
    files = []
 
    for file in os.listdir(path): # lists all files + directories in specified directory
        ext = os.path.splitext(file)[1] # splits directory name into [root, ext]
        if ext.lower() in extensions:
            files.append(file)

    if not folder in os.listdir(path): os.mkdir(os.path.join(path, folder))

    for file in files:
        os.rename(os.path.join(path, file), os.path.join(os.path.join(path, folder), file))

base_path = "/Users/daniel/"
folders = ["Desktop", "Downloads"]
visual_extensions = [".jpg", ".jpeg", ".png", ".raw" ".gif", ".mp4", ".mov", ".wmv", ".avi", ".flv"]
doc_extensions = [".pdf", ".doc", ".docx", ".txt", ".rtf", ".html", ".ppt", ".pptx", ".xls", "xlsx"]
media_types = [(visual_extensions, "Photos:Videos"), (doc_extensions, "Documents")]

for folder in folders:
    for media in media_types:
        organize(os.path.join(base_path, folder), media[0], media[1])

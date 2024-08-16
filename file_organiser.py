import os
import shutil

def file_organiser(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]

    for file in files:
        file_extension = os.path.splitext(file)[1][1:]
        folder_name = file_extension.upper() + "_FILE"

    if not os.path.exists(os.path.join(folder_path,folder_name)):
        os.makedirs(os.path.join(folder_path,folder_name))
    
    shutil.move(os.path.join(folder_path,file),os.path.join(folder_path,folder_name,file))

    print("File organiser complete!")


folder_path = "D:/Desktop/proiecte/file_organiser/files"

file_organiser(folder_path)

    
    
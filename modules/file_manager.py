# file_manager.py

import os

def create_folder(folder_name, path="."):
    full_path = os.path.join(path, folder_name)
    try:
        os.makedirs(full_path, exist_ok=True)
        return f"Folder created at: {full_path}"
    except Exception as e:
        return f"Error creating folder: {e}"

def create_file(file_name, path=".", content=""):
    full_path = os.path.join(path, file_name)
    try:
        with open(full_path, 'w') as file:
            file.write(content)
        return f"File created at: {full_path}"
    except Exception as e:
        return f"Error creating file: {e}"

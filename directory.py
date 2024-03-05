import os

def list_directories_and_files(path):
    if os.path.exists(path):
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        
        print("Directories:", directories)
        print("Files:", files)
        print("All Directories and Files:", os.listdir(path))
    else:
        print("Specified path does not exist.")
specified_path = "c:\wert"
list_directories_and_files(specified_path)

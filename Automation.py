import os
import shutil

# Define the directory you want to organize
directory = r"C:\Users\DELL\Desktop\Automation Test"

# Create folders for different file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov"],
}

# Create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to the respective folders
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, folder, file_name))
                break

print("Files organized successfully!")

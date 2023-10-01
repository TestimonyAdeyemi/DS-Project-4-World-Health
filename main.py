import os

# Replace 'your_folder_path' with the path to your folder
folder_path = 'DataSets'
new_extension = '.xlsx'

# List all files in the folder
files = os.listdir(folder_path)

# Loop through the files and rename them
for file in files:
    # Check if the file has the old extension you want to change
    if file.endswith('.csv'):
        # Construct the new file name with the desired extension
        new_name = os.path.splitext(file)[0] + new_extension
        # Rename the file
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

print("File extensions have been changed to .xlsx.")

import os
import shutil

# Create a subdirectory
os.makedirs('new_subdirectory', exist_ok=True)

# Copy a file
source_file = 'source.txt'
destination_file = 'new_subdirectory/copied_file.txt'
shutil.copy(source_file, destination_file)

print(f"File copied to {destination_file}.")
print("Hello World")
import os

# Create three new folders
os.makedirs("folder1", exist_ok=True)
os.makedirs("folder2", exist_ok=True)
os.makedirs("folder3", exist_ok=True)

# Navigate inside folder1 and create three new folders
os.makedirs("folder1/subfolder1", exist_ok=True)
os.makedirs("folder1/subfolder2", exist_ok=True)
os.makedirs("folder1/subfolder3", exist_ok=True)

# Remove two folders from folder1
try:
    os.rmdir("folder1/subfolder2")
    os.rmdir("folder1/subfolder3")
except FileNotFoundError:
    pass



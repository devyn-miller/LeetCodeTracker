import os

def print_directory_structure(directory, indent=''):
    print(indent + os.path.basename(directory) + '/')
    indent += '│   '
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print_directory_structure(item_path, indent + '│   ')
        else:
            print(indent + '├── ' + item)

# Replace 'directory_path' with the path to your project directory
directory_path = 'LeetCodeTracker'  # Example directory path

print_directory_structure(directory_path)


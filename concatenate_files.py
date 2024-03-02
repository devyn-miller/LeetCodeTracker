import os

def concatenate_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for foldername, _, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')  # Add a newline between files

# Replace 'directory_path' with the path to your project directory
directory_path = 'LeetCodeTracker'  # Example directory path
output_file_path = 'project_text.txt'  # Path to save the concatenated text file

concatenate_files(directory_path, output_file_path)

print("Project files concatenated into:", output_file_path)

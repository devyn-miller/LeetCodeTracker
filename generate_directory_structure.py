import os

folders = [
    "LeetCodeTracker/app",
    "LeetCodeTracker/app/models",
    "LeetCodeTracker/app/routes",
    "LeetCodeTracker/app/templates",
    "LeetCodeTracker/app/static/css",
    "LeetCodeTracker/app/static/js",
    "LeetCodeTracker/migrations",
]

files = {
    "LeetCodeTracker/app/__init__.py": "",
    "LeetCodeTracker/app/models/__init__.py": "",
    "LeetCodeTracker/app/models/models.py": "",  # We'll fill this in later
    "LeetCodeTracker/app/routes/__init__.py": "",
    "LeetCodeTracker/app/routes/auth.py": "",  # To be filled
    "LeetCodeTracker/app/routes/main.py": "",  # To be filled
    "LeetCodeTracker/app/templates/layout.html": "",  # Basic HTML structure
    "LeetCodeTracker/app/templates/index.html": "",  # Home page
    "LeetCodeTracker/app/templates/login.html": "",  # Login form
    "LeetCodeTracker/app/templates/register.html": "",  # Registration form
    "LeetCodeTracker/app/static/css/style.css": "",  # CSS Styles
    "LeetCodeTracker/app/static/js/script.js": "",  # JS Scripts
    "LeetCodeTracker/config.py": "",  # Configuration settings
    "LeetCodeTracker/run.py": "",  # Entry point to start the Flask app
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, file_content in files.items():
    with open(file_path, "w") as f:
        f.write(file_content)

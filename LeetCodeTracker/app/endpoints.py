from flask import Flask, jsonify
from . import db  # Import your database setup from __init__.py
from .models.models import UserProgress  # Import your UserProgress model

app = Flask(__name__)

@app.route('/api/user_progress/<int:user_id>')
def user_progress(user_id):
    # Example function call to get user progress data from the database
    progress_data = get_user_progress(user_id)
    
    # Convert progress_data to JSON and return
    return jsonify(progress_data)

def get_user_progress(user_id):
    # Placeholder for fetching user progress data from your database
    # This is where you would query your UserProgress model
    # For now, returning a mock response
    return {
        "user_id": user_id,
        "progress": [
            {"problem_id": 1, "success": True, "time_spent": 120, "attempts": 1},
            {"problem_id": 2, "success": False, "time_spent": 300, "attempts": 3}
        ]
    }

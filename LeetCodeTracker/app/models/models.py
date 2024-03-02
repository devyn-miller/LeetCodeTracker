from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # Additional fields as necessary

class LeetCodeProblem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)
    # Additional fields

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('leet_code_problem.id'), nullable=False)
    success = db.Column(db.Boolean, nullable=False)
    time_spent = db.Column(db.Integer, nullable=False)  # Time in seconds
    user_difficulty_rating = db.Column(db.Integer, nullable=False)
    # Timestamps, etc.

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from ..models.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # Logic for login verification
    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return render_template('register.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # Logic for registering a new user
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    # Logic for logging out
    return redirect(url_for('main.index'))

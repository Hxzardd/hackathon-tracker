from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__, template_folder='../frontend')

@dashboard.route('/dashboard', methods=['GET'])
@login_required
def show_dashboard():
    # Replace with dynamic data from your database if needed
    user = {
        'name': current_user.username,
        'reg_no': '123456',
        'skills': 'Python, Flask, JavaScript'
    }
    return render_template('dashboard.html', user=user)

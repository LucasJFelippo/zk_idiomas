from flask import Blueprint, render_template, abort


base = Blueprint('base', __name__, template_folder='templates')

@base.route('/')
def index():
    return render_template('base_home.html')
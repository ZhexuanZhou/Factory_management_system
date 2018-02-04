from flask import render_template
from flask_login import login_required
from ..decorators import permission_required, admin_required
from . import main


@main.route('/')
@main.route('/index')
@login_required
@admin_required
# @permission_required(Permission.MODERATE_COMMENTS)
def index():
    # user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # return render_template('index.html', title='Home', user=user, posts=posts)
    return render_template("index.html", title='Home Page', posts=posts)




from flask import render_template, session, redirect, url_for, current_app
from . import main
from flask_login import login_required
from app.decorators import permission_required, admin_required
from ..models import Permission


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return 'for administrators only!'


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return 'for comment moderators only'

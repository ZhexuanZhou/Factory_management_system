from . import api
from ..decorators import admin_required
from flask_login import login_required


@api.route('/property/index')
@login_required
@admin_required
def p_index():
    return 'property index'

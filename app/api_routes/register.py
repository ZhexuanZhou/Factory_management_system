from . import api


@api.route('/register/index/')
def r_index():
    return 'register index'

from . import api


@api.route('/user/index/')
def u_index():
    return 'user index'

from . import api


@api.route('/server/index/')
def s_index():
    return 'server index'

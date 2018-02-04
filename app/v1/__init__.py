# [START Imports]
from controllers.home import home
# [END Imports]

def configure_paths(app):
    app.template_folder = 'app/v1/views/templates'
    app.static_folder = 'app/v1/views/static'


def configure_blueprints(app):
    app.register_blueprint(home)
# [START Imports]
import os
import sys
from app.v1.controllers.home import home
from flask import Flask, url_for
# [END Imports]

app = Flask(__name__)

# [START Configurations]
sys.path.append(os.path.abspath(os.getcwd()))
app.template_folder = 'app/v1/views/templates'
app.static_folder = 'app/v1/views/static'

# [START Cache Buster]

# [END Cache Buster]

# [START Blueprints]
app.register_blueprint(home)
# [END Blueprints]

app.debug = True
# [END Configurations]

# [START Run]
if __name__ == '__main__':
    app.run()
# [END Run]
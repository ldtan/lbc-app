# [START Imports]
import os
import sys
from app import v1
from flask import Flask, url_for
# [END Imports]

app = Flask(__name__)

# [START Configurations]
sys.path.append(os.path.abspath(os.getcwd()))

v1.configure_paths(app)
v1.configure_blueprints(app)

app.debug = True
# [END Configurations]

# [START Run]
if __name__ == '__main__':
    app.run()
# [END Run]
# [START Imports]
import os
import sys
from app import v1
from flask import Flask, render_template, url_for
from werkzeug import exceptions
# [END Imports]

app = Flask(__name__)

# [START Configurations]
sys.path.append(os.path.abspath(os.getcwd()))

v1.configure_paths(app)
v1.configure_blueprints(app)

app.debug = True
# [END Configurations]

# [START Error Handler]
@app.errorhandler(404)
def handle_error(error):
    return render_template('error.html', error=error)
# [END Error Handler]

# [START Run]
if __name__ == '__main__':
    app.run()
# [END Run]
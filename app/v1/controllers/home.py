# [START Imports]
from flask import Blueprint, render_template
# [END Imports]

home = Blueprint('home', __name__, url_prefix='/home')

# [START Controllers]
@home.route('/', methods=['GET'])
def read():
    return render_template('home.html')
# [END Controllers]
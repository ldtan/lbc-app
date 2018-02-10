# [START Imports]
from flask import Blueprint, abort, render_template
# [END Imports]

about_us = Blueprint('about_us', __name__)

# [START Controllers]
@about_us.route('/<string:page>/')
def read(page):
    pages = {
        'about_us': 'about_us.html',
        'pastors_corner': 'pastors_corner.html',
        'our_history': 'our_history.html',
        'faith_promise_mission': 'faith_promise_mission.html',
        'world_missions': 'world_missions.html',
        'building_project': 'building_project.html',
        'services': 'services.html',
        'contact_us': 'contact_us.html'
    }

    if pages.get(page, None) is None:
        abort(404)

    return render_template(pages[page])


# @about_us.route('/about_us/', methods=['GET'])
# def read_about_us():
#     return render_template('about_us.html')


# @about_us.route('/pastors_corner/', methods=['GET'])
# def read_pastors_corner():
#     return render_template('pastors_corner.html')


# @about_us.route('/our_history/', methods=['GET'])
# def read_our_history():
#     return render_template('our_history.html')


# @about_us.route('/faith_promise_mission/', methods=['GET'])
# def read_faith_promise_mission():
#     return render_template('faith_promise_mission.html')


# @about_us.route('/world_missions/', methods=['GET'])
# def read_world_missions():
#     return render_template('world_missions.html')


# @about_us.route('/building_project/', methods=['GET'])
# def read_building_project():
#     return render_template('building_project.html')


# @about_us.route('/services/', methods=['GET'])
# def read_services():
#     return render_template('services.html')


# @about_us.route('/contact_us/', methods=['GET'])
# def read_contact_us():
#     return render_template('contact_us.html')
# [END Controllers]
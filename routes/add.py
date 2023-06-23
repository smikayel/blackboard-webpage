from flask import Blueprint, request, render_template
from services.blackboard_service import BlackboardApi


add_rout = Blueprint('add', __name__)


@add_rout.route('/add_user', methods=['POST'])
def add_handler():
    context = {}
    try:
        role = request.form['role']
        course_id = request.form['course_id']
        user_id = request.form['user_id']
        api = BlackboardApi()
        print(role)
        res = api.make_post_request(course_id, user_id, role)

    except Exception as e:
        print(e)

    return render_template("index.html", context=context)
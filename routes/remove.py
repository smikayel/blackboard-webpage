from flask import Blueprint, request, render_template
from services.blackboard_service import BlackboardApi

remove = Blueprint('remove_user', __name__)


@remove.route('/remove_user', methods=['POST'])
def remove_handler():
    context = {}
    try:
        course_id = request.form['course_id']
        user_id = request.form['user_id']
        api = BlackboardApi()
        res = api.make_delete_request(course_id, user_id)

    except Exception as e:
        print(e)

    return render_template("index.html", context=context)
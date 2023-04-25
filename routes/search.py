from flask import Blueprint, request, render_template
from services.blackboard_service import BlackboardApi


search = Blueprint('search', __name__)


@search.route('/search', methods=['POST'])
def search_handler():
    course_name = request.form['courseName']
    user_ame = request.form['userName']
    api = BlackboardApi()

    user = api.search_user(user_ame)
    course = api.search_course(course_name)
    context = {'user': [], 'user_count': 0, 'course': [], 'course_count': 0}
    if user:
        context['user'] = user
        context['user_count'] = len(user)
    if course:
        context['course'] = course
        context['course_count'] = len(course)
    # Do something with the input value
    return render_template("index.html", context=context)
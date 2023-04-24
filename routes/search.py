from flask import Blueprint, request

search = Blueprint('search', __name__)


@search.route('/search', methods=['POST'])
def search_handler():
    course_name = request.form['courseName']
    user_ame = request.form['userName']



    # Do something with the input value
    return f"You entered: {course_name, user_ame}"
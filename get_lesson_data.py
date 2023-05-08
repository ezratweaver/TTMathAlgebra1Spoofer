from sqlite3 import connect
from os import path, environ, chdir
from get_average import get_average

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"

def grab_lesson_data(test=False):
    tt_math_dir = path.join(environ["PUBLIC"], "Documents", PUBLIC_FOLDER)
    chdir(tt_math_dir)
    database_connection = connect(DATABASE_NAME)
    cursor = database_connection.cursor()

    sql_execute = "SELECT LNum, LScore FROM userLessonGrade_2 ORDER BY LNum ASC"
    if test:
        sql_execute = "SELECT QNum, QScore FROM userQuizGrade_2 ORDER BY QNum ASC"

    cursor.execute(sql_execute)
    number_and_score = cursor.fetchall()
    cursor.close()
    database_connection.close()
    return number_and_score

def sift_lesson_data(input_data, max_lessons):
    grade_to_percentage = {
            "A+": 97,
            "A": 93,
            "A-": 90,
            "B+": 87,
            "B": 83,
            "B-": 80,
            "C+": 77,
            "C": 73,
            "C-": 70,
            "D+": 67,
            "D": 63,
            "D-": 60,
            "F": 0,
        }

    total_lessons = 0
    total_percentage = 0
    for lesson in input_data:
        split_lesson_data = [int(x) for x in lesson[1].split(" | ")[10:]]
        problem_correct = 0
        problem_wrong = 0
        for number in split_lesson_data:
            if number == 1:
                problem_correct += 1
            elif number == 0:
                problem_wrong += 1
        try:
            grade_percentage = get_average(
                            problem_correct, 
                            problem_correct + problem_wrong)
        except ZeroDivisionError:
            grade_percentage = 0
        if problem_correct + problem_wrong > 0:
            total_lessons += 1
        total_percentage = total_percentage + grade_percentage
    for grade in sorted(grade_to_percentage.keys()):
        if get_average(total_percentage, total_lessons) >= grade_to_percentage[grade]:
            grade = grade
            break

    if total_lessons > max_lessons:
        total_lessons = max_lessons

    progress = f"{total_lessons}/{max_lessons}"
    progress_percentage = f"{get_average(total_lessons, max_lessons)}%"
    grade_percentage = f"{get_average(total_percentage, total_lessons)}%"
    return progress, progress_percentage, grade, grade_percentage

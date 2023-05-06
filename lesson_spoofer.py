from string_injector import inject_lesson
from problem_counter import find_problem_count
from string_generator import generate_lesson_string

def spoof_lesson(lesson, add_wrong, test=False):
    problem_count = find_problem_count(lesson)
    if test:
        problem_count = 25
    Num = str(lesson)
    Score = generate_lesson_string('1', '-1', problem_count, test, add_wrong=add_wrong)
    Trial = generate_lesson_string('1', '10', problem_count, test)
    UserAns = generate_lesson_string('', '', problem_count, test)
    CorrectAns = generate_lesson_string('True', '', problem_count, test)
    ViewedSolns = generate_lesson_string('0', '0', problem_count, test)

    inject_lesson(Num,
                Score, Trial, UserAns,
                CorrectAns, ViewedSolns, test)

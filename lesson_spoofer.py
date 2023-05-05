from string_injector import inject_lesson
from problem_counter import find_problem_count
from string_generator import generate_lesson_string

def spoof_lesson(lesson, add_wrong):
    problem_count = find_problem_count(lesson)
    LNum = str(lesson)
    LScore = generate_lesson_string('1', '-1', problem_count, add_wrong=add_wrong)
    LTrial = generate_lesson_string('1', '10', problem_count)
    LUserAns = generate_lesson_string('', '', problem_count)
    LCorrectAns = generate_lesson_string('True', '', problem_count)
    LViewedSolns = generate_lesson_string('0', '0', problem_count)

    inject_lesson(LNum,
                LScore, LTrial, LUserAns,
                LCorrectAns, LViewedSolns)
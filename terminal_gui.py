from math import floor

def create_progress_bar(progress):
    progress = int(progress[:-1])
    progress = floor(progress / 5)
    string = "=" * progress
    string = string + (" " * (20 - progress))
    string = "|" + string + "|"
    return string

def print_gui(lesson_numbers, lesson_percentage,
              grade_letter, grade_percentage):
    
    lesson_progress_bar = create_progress_bar(lesson_percentage)
    grade_progress_bar = create_progress_bar(grade_percentage)

    print(f"Lessons: {lesson_numbers}               Grade: {grade_letter}")
    print("----------------------         ----------------------")
    print(f"{lesson_progress_bar} {lesson_percentage}     {grade_progress_bar} {grade_percentage}")
    print("----------------------         ----------------------")
from os import system 
from time import sleep
from problem_counter import db_connection
from lesson_spoofer import spoof_lesson
from get_lesson_data import grab_lesson_data, sift_lesson_data

ADD_WRONG = True

lesson_data = grab_lesson_data()
progress, progress_percentage, grade_percentage, grade = sift_lesson_data(
    lesson_data)

system('cls')
print('Welcome to Teaching Textbooks Algebra 1 Lesson Spoofer\n')
print(f"Current Progress: {progress} ({progress_percentage})")
print(f"Current Grade: {grade_percentage} ({grade})\n")

user_input_lesson_start = int(input("Type starting lesson >>> "))
user_input_lesson_end = int(input("Type ending lesson >>> "))

system('cls')
for x in range(user_input_lesson_start, user_input_lesson_end + 1):
    print(f"Spoofing Lesson {x}...")
    sleep(1)
    spoof_lesson(x, ADD_WRONG)

system('cls')
print(f'Done! Spoofed lessons {user_input_lesson_start}-{user_input_lesson_end}')

db_connection.close()
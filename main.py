from os import system 
from time import sleep
from problem_counter import db_connection
from lesson_spoofer import spoof_lesson
from get_lesson_data import grab_lesson_data, sift_lesson_data
from terminal_gui import print_gui

lesson_data = grab_lesson_data()
test_data = grab_lesson_data(test=True)
lesson_variables = sift_lesson_data(lesson_data, 142)
test_variables = sift_lesson_data(test_data, 19)

def error(message):
    system('cls')
    print(f'Error: {message}')
    quit()

system("cls")
print("Welcome to Teaching Textbooks Algebra 1 Lesson Spoofer\n")

print("[1] Lessons\n[2] Tests\n")

user_confirm_spoof = input("What would you like to spoof? ")

system("cls")

if user_confirm_spoof == "1":
    spoof_type = 'Lesson'
    spoof_variable = lesson_variables[0]
    user_input_test = False
    print_gui(*lesson_variables)
elif user_confirm_spoof == "2":
    spoof_type = 'Test'
    spoof_variable = test_variables[0]
    user_input_test = True
    print_gui(*test_variables)
else:
    error("Invalid Input")

user_lesson_start = int(input(f"\nType starting {spoof_type} >>> "))
if user_lesson_start <= int(spoof_variable.split("/")[0]):
    error(f"Starting Lesson Lower Then {spoof_type} Completed")
user_lesson_end = int(input(f"Type ending {spoof_type} >>> "))
user_addwrong = input("Spoof Incorrect Problems? (Y/N) ")

if user_addwrong.upper() == 'Y':
    user_addwrong = True
else:
    user_addwrong = False

system("cls")
for x in range(user_lesson_start, user_lesson_end + 1):
    print(f"Spoofing {spoof_type} {x}...")
    sleep(1)
    spoof_lesson(x, user_addwrong, test=user_input_test)

system("cls")
print(f"Done! Spoofed {spoof_type} {user_lesson_start}-{user_lesson_end}")

db_connection.close()

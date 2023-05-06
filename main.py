from os import system 
from time import sleep
from problem_counter import db_connection
from lesson_spoofer import spoof_lesson
from get_lesson_data import grab_lesson_data, sift_lesson_data

lesson_data = grab_lesson_data()
test_data = grab_lesson_data(test=True)
Lprogress, Lprogress_percentage, Lgrade_percentage, Lgrade = sift_lesson_data(
    lesson_data, 142)
Tprogress, Tprogress_percentage, Tgrade_percentage, Tgrade = sift_lesson_data(
    test_data, 19)

system("cls")
print("Welcome to Teaching Textbooks Algebra 1 Lesson Spoofer\n")
print(f"Lesson Progress: {Lprogress} ({Lprogress_percentage})")
print(f"Lesson Grade: {Lgrade_percentage} ({Lgrade})\n")
print(f"Test Progress: {Tprogress} ({Tprogress_percentage})")
print(f"Test Grade: {Tgrade_percentage} ({Tgrade})\n")

user_input_confirm_spoof = input("Do you want to spoof? (Y/N) ")
user_input_test = input("Spoof Tests? (Y/N) ")
user_input_addwrong = input("Spoof Incorrect Problems? (Y/N) ")

if user_input_test.upper() == "Y":
    user_input_test = True
    spoof_type = 'test'
else:
    user_input_test = False
    spoof_type = 'lesson'
if user_input_addwrong.upper() == "Y":
    user_input_addwrong = True
else:
    user_input_addwrong = False

if user_input_confirm_spoof.upper() == "Y":
    system("cls")
    user_input_lesson_start = int(input(f"Type starting {spoof_type} >>> "))
    user_input_lesson_end = int(input(f"Type ending {spoof_type} >>> "))
else:
    system("cls")
    quit()

system("cls")
for x in range(user_input_lesson_start, user_input_lesson_end + 1):
    print(f"Spoofing {spoof_type} {x}...")
    sleep(1)
    spoof_lesson(x, user_input_addwrong, test=user_input_test)

system("cls")
print(f"Done! Spoofed {spoof_type} {user_input_lesson_start}-{user_input_lesson_end}")

db_connection.close()

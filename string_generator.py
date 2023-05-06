from random import randint

def generate_lesson_string(first_number, second_number,
                           problem_count, test, add_wrong=False):
    if test:
        list = [first_number] * (problem_count + 15)
        list[problem_count:] = [second_number] * 15
    else:
        list = [first_number] * (problem_count + 20)
        list[5:10] = [second_number] * 5
        list[problem_count + 10:] = [second_number] * 10
    if add_wrong:
        amount_wrong = randint(0, 2)
        for x in range(amount_wrong):
            random_index = randint(10, problem_count)
            list[random_index:random_index+1] = ['0'] * 1
    string = ' | '.join(list)
    return string

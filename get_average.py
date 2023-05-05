def get_average(test_group, total_group):
    answer = test_group / total_group
    if answer <= 1:
        return int(round(answer * 100))
    return int(round(answer))

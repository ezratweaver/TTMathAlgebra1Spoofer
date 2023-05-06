from sqlite3 import connect
db_connection = connect('problemset.db')

def find_problem_count(lesson):
    cursor = db_connection.cursor()
    cursor.execute('SELECT problemID FROM solutionFile WHERE lessonID = ?', (lesson,))
    results = cursor.fetchall()

    counter = 0
    for row in results:
        try:
            int(row[0])
        except ValueError:
            continue
        counter += 1
    return counter

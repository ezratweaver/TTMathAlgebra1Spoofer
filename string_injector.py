from os import path, environ, chdir
from sqlite3 import connect

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"

def inject_lesson(LNum, LScore, LTrial, 
                  LUserAns, LCorrectAns, LViewedSolns):
    tt_math_dir = path.join(environ["PUBLIC"], "Documents", PUBLIC_FOLDER)
    chdir(tt_math_dir)
    db_connection = connect(DATABASE_NAME)
    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO userLessonGrade_2 (LNum, LScore, LTrial, LUserAns, LCorrectAns, LViewedSolns) VALUES (?, ?, ?, ?, ?, ?)",
                    (LNum, LScore, LTrial, LUserAns, LCorrectAns, LViewedSolns))
    db_connection.commit()
    db_connection.close()

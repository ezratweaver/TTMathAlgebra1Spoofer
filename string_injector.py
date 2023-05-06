from os import path, environ, chdir
from sqlite3 import connect

DATABASE_NAME = "algebra1dat"
PUBLIC_FOLDER = "TT Algebra 1"

def inject_lesson(Num, Score, Trial, 
                  UserAns, CorrectAns, ViewedSolns, Test=False):
    tt_math_dir = path.join(environ["PUBLIC"], "Documents", PUBLIC_FOLDER)
    chdir(tt_math_dir)
    db_connection = connect(DATABASE_NAME)
    cursor = db_connection.cursor()


    sql_execute = "INSERT INTO userLessonGrade_2 (LNum, LScore, LTrial, LUserAns, LCorrectAns, LViewedSolns) VALUES (?, ?, ?, ?, ?, ?)"
    if Test:
        sql_execute = "INSERT INTO userQuizGrade_2 (QNum, QScore, QTrial, QUserAns, QCorrectAns, QViewedSolns) VALUES (?, ?, ?, ?, ?, ?)"

    cursor.execute(sql_execute,
                    (Num, Score, Trial, UserAns, CorrectAns, ViewedSolns))
    db_connection.commit()
    db_connection.close()

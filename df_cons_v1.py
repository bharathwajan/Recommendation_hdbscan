import pandas as pd
import mysql.connector as mysql
# class extractor():
def extractor():
    try:
        conn = mysql.connect(host='localhost', database='laravel_test', user='root', password='root')
        cursor = conn.cursor()
        #obtaining records
        q1="SELECT * FROM posts where source_id=1"
        cursor.execute(q1)
        result = cursor.fetchall()
        #obtaining column names
        q2="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'posts' ORDER BY ORDINAL_POSITION;"
        cursor.execute(q2)
        col_names = cursor.fetchall()
        fin_col_names=[]
        for tup in col_names:
            fin_col_names.append(tup[0])
        return pd.DataFrame(result,columns=fin_col_names),"################hello##########"
        # return "hello"

    except:
        return "error connecting to local db server"
    
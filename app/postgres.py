import psycopg2 as database
from psycopg2.extras import execute_values
from constants import query


'''
This function convert the record objects to tuples and return them as a list. This will make it easier to add to the database.
'''
def create_list_of_tuples(records):
    tupleList = [record.tuple for record in records]
    return tupleList


'''
This function will connect to the database and add the data to the database.
'''

def add_data(kwargs, records):
    conn = database.connect(**kwargs)
    cur = conn.cursor()
    tuples_record = create_list_of_tuples(records)
    execute_values(cur, query, tuples_record)
    conn.commit()
    cur.close()
    conn.close()




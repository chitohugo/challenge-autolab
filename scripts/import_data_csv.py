import csv
import sqlite3
from datetime import datetime

DB = '../dev.sqlite3'


def connection():
    """Method to connect to sqlite database

    Returns:
        returns a connection object

    Raises:
        Error: An error occurred.
    """
    try:
        return sqlite3.connect(DB)
    except sqlite3.Error as er:
        raise er


def reader_csv(file_name):
    """Method to read the csv file

    Args:
        file_name: file name in .csv format

    Returns:
        data_lists: A list of tuples with the data from the file.

    Raises:
        IOError: An error occurred accessing the file.
    """
    try:
        with open(str(file_name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = next(csv_reader)
            data_list = []
            created_on = datetime.now()
            updated_on = datetime.now()
            _id = 1

            for row in csv_reader:
                data_list.append((_id, created_on, updated_on, row[1], row[2],
                                  row[3], row[4], row[5], row[6], row[7], row[8],
                                  row[9], row[10], row[11], row[12]
                                  )
                                 )
                _id += 1
    except IOError as er:
        raise er
    return data_list


def insert_data(data, connect):
    """Method to insert the data in the pokemon table

    Args:
        data: A list of tuples with the data from the file
        connect: Sqlite connection object

    Returns:
        True if the data was saved successfully

    Raises:
        Error: An error occurred.
    """
    cursor = connect.cursor()
    try:
        cursor.executemany(
            "insert into pokemon VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
        connect.commit()
        print("Successfully saved...")
    except sqlite3.Error as er:
        raise er

    connect.close()


if __name__ == "__main__":
    connect = connection()
    data = reader_csv("file/pokemon.csv")
    insert_data(data, connect)

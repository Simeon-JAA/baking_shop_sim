"""Handles all functions that connect and interact with a db"""

from os import environ
from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extensions import connection


def get_db_connection(config) -> connection:
    """Returns a connection to the db"""
    try:
        conn = connect(dbname=config["dbname"],
                       host=config["host"],
                       user=config["user"])

    except (ConnectionError, ConnectionAbortedError) as Err:
        Err("Error: Unable to establish connection to the database!")

    return conn


# TODO Check return type hint
def check_user_email_in_db(user_email: str, conn: connection) -> bool:
    """Function will return true if user email address found in db
     If not, the function will return false"""

    cur = conn.cursor()

    cur.execute(f"""SELECT user_name FROM baking_sim_user
                WHERE user_email = '{user_email}';""")

    data = cur.fetchall()

    cur.close()

    if data == []:
        return False

    return True


def get_user_id_from_email_and_password(user_email: str, user_password: str, conn: connection) -> int:
    """Returns the user_id based on user_email and password"""

    if not check_user_email_in_db(user_email, conn):
        raise KeyError("Error: This email is not registered on the database!")

    cur = conn.cursor()

    cur.execute(f"""SELECT baking_sim_user_id FROM baking_sim_user
                WHERE user_email = '{user_email}'
                AND user_password = '{user_password}';""")

    data = cur.fetchall()

    cur.close()

    if not data:
        raise ValueError("Error: Incorrect password!")

    return data[0][0]


if __name__ == "__main__":

    load_dotenv()

    config = environ

    try:
        conn = get_db_connection(config)
    except ConnectionError as Err:
        Err("Error: Unable to establish connection to database!")

    print(get_user_id_from_email_and_password(
        "example_email@example.co.uk", "example_password", conn))

    conn.close()

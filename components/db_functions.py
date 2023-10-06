"""Handles all functions that connect and interact with a db"""

from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extensions import connection


def get_db_connection(config) -> connection:
    """Returns a connection to the db"""

    return


if __name__ == "__main__":
    get_db_connection()

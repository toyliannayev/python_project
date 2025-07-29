import mysql.connector
import dotenv
from pathlib import Path
import os

dotenv.load_dotenv(Path('.env'))

db_config_read = {'host':os.environ.get('host_read'),
                  'user': os.environ.get('user_read'),
                  'password': os.environ.get('password_read'),
                  'database': 'sakila'
                  }
conn_read = mysql.connector.connect(**db_config_read)
cursor_read = conn_read.cursor()

db_config_write = {'host': os.environ.get('host_write'),
                   'user': os.environ.get('user_write'),
                   'password': os.environ.get('password_write'),
                   'database': 'group_111124_fp_Toyli_Annayev'
                   }

conn_write = mysql.connector.connect(**db_config_write)
cursor_write = conn_write.cursor()


def get_db_edit_connection():
    return conn_write, cursor_write




import psycopg2
from psycopg2 import pool
import config
pool = psycopg2.pool.SimpleConnectionPool( 
    3, 5,database = config.db_database, 
                        user = config.db_user, 
                        host= config.db_host,
                        password = config.db_password,
                        port = config.db_port)

# conn = psycopg2.connect(database = config.db_database, 
#                         user = config.db_user, 
#                         host= config.db_host,
#                         password = config.db_password,
#                         port = config.db_port)



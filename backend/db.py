import psycopg2
import config
conn = psycopg2.connect(database = config.db_database, 
                        user = config.db_user, 
                        host= config.db_host,
                        password = config.db_password,
                        port = config.db_port)



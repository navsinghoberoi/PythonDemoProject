import pymysql
import AppiumBasics.db_config as config

def connect_db(dbname):
    if dbname != config.DATABASE_CONFIG["dbname"]:
        raise ValueError("Couldn't not find database with given name")
    else:
        db = pymysql.connect(host = config.DATABASE_CONFIG["host"],
                             user=config.DATABASE_CONFIG["user"],
                             password=config.DATABASE_CONFIG["password"],
                             db=config.DATABASE_CONFIG["dbname"])

        return db


try:
    db_conn = connect_db("USER_MANAGEMENT_SYSTEMS")
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM USERS WHERE USER_ID = 652245")
    data = cursor.fetchone()
except:
    print("Exception while creating db connection")
print ("Data fetched from db = ", data)

db_conn.close()




import mysql.connector
from configmodule.config import config

mydb = mysql.connector.connect(
    host=config["database"]["host"],
    user=config["database"]["user"],
    passwd=config["database"]["passwd"],
    database=config["database"]["database"])


def get_user_id(name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM users where name='{0}'".format(name))
    myresult = mycursor.fetchone()[0]
    return myresult


def get_transactions(userid):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT name, amount, description FROM transactions where userid='{0}'".format(userid))
    myresult = mycursor.fetchall()
    return myresult


def get_user_channels(user_id):
    mycursor = mydb.cursor()
    sql = "SELECT `channel`, `type` FROM channels INNER JOIN `user_channels` ON " \
          "`user_channels`.channel_id = channels.`id` WHERE user_id={0}".format(user_id)
    mycursor.execute(sql)
    response = mycursor.fetchall()
    return response


def get_channel_type(channel):
    mycursor = mydb.cursor()
    sql = "SELECT type FROM channels WHERE channel='{0}'".format(channel)
    mycursor.execute(sql)
    response = mycursor.fetchone()[0]
    return response


def insert_financial_data(user_id, channel, aggregation_date, data):
    mycursor = mydb.cursor()
    sql = "INSERT INTO user_channel_transactions (user_id, channel, last_aggregation_date, transactions_list, balance) " \
          "VALUES (%s, %s, %s, %s, %s)"
    print(data['balance'])
    val = (user_id, channel, aggregation_date, str(data['transactions']), data['balance'])
    mycursor.execute(sql, val)
    mydb.commit()


def insert_financial_data_list(user_id, channel, aggregation_date, data_list):
    mycursor = mydb.cursor()
    # turn autocommit off to enable bulk insert
    mycursor.execute("SET autocommit=0")
    for data in data_list:
        sql = "INSERT INTO user_channel_transactions (user_id, channel, last_aggregation_date, transactions_list, balance) " \
              "VALUES (%s, %s, %s, %s, %s)"
        val = (user_id, channel, aggregation_date, str(data['transactions']), data['balance'])
        mycursor.execute(sql, val)
    mydb.commit()


def get_statements(user_id):
    cursor = mydb.cursor()
    sql = "SELECT statement from user_statements where user_id = {0}".format(user_id)
    cursor.execute(sql)
    return cursor.fetchall()

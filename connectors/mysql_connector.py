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


def set_api_transactions(userid, transactions_list):
    mycursor = mydb.cursor()
    sql = "INSERT INTO transactions (user_id, name, amount, description) VALUES (%s, %s, %s, %s)"
    for transaction in transactions_list:
        val = (userid, transaction["name"], transaction["amount"], transaction["description"])
        mycursor.execute(sql, val)
    mydb.commit()


def set_web_transactions(userid, transactions_list):
    mycursor = mydb.cursor()
    sql = "INSERT INTO transactions (user_id, name, amount, description) VALUES (%s, %s, %s, %s)"
    for transaction in transactions_list:
        val = (userid, transaction["Id"], transaction["Balance"], transaction["description"])
        mycursor.execute(sql, val)
    mydb.commit()


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

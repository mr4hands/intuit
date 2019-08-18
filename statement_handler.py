from connectors import mysql_connector


# assuming that statements are saves as binary, the binary just get pulled from db and sent to the client
def get_statments(user_id):
    statement = mysql_connector.get_statements(user_id)
    return {'statment': statement}

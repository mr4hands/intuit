def validate_types(user_id, channel):
    if not isinstance(user_id, str):
        raise TypeError("user_id is not of type {0}".format("string"))
    if not isinstance(channel, str):
        raise TypeError("channel is not of type {0}".format("string"))
def validate_types(user_id, channel, on_demand):
    if not isinstance(user_id, str):
        raise TypeError("user_id is not of type {0}".format("string"))
    if not isinstance(channel, str):
        raise TypeError("channel is not of type {0}".format("string"))
    if not isinstance(on_demand, bool):
        raise TypeError("on_demand is not of type {0}".format("bool"))
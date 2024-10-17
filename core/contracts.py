user_data_scheme = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "integer"},
        "email" : {"type" : "string"},
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"},
        "avatar" : {"type" : "string"},
    },
    "required" : ["id", "email", "first_name", "last_name", "avatar"]
}
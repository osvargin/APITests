user_data_scheme = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

resource_data_scheme = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "year": {"type": "integer"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}

create_user_scheme = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["id"]
}

update_user_scheme = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    }
}
register_and_login_scheme = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

register_unsuccessful_scheme = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

login_successful_scheme = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

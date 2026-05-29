from app.data.users import users

def register_user(data):
    users.append(data)

def authenticate_user(email, password):
    return next(
        (
            user
            for user in users
            if user["email"] == email
            and user["password"] == password
        ),
        None
    )
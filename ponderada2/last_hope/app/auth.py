from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
import database

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'auth_token' in request.cookies:
            token = request.cookies['auth_token']
            user_id = request.cookies['user_id']
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            print("TOKEN: ", token)
            key = "be7e1ac39b5a29e541c551a3ebb165c5"
            data = jwt.decode(token, key, algorithms=["HS256"])
            current_user = table_creation.User.query.filter_by(id=user_id).first()
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
            else:
                current_user = {
                "id": user_id,
                "token": token
            }
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated
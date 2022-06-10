import calendar
import datetime

import jwt

from constants import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES, TOKEN_EXPIRE_DAYS


def approve_tokens(user_data):
    try:
        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
        user_data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(user_data,
                                  key=SECRET_KEY, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
        user_data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(user_data,
                                   key=SECRET_KEY, algorithm=ALGORITHM)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
    except jwt.PyJWTError as e:
        return f"{e}"
    return tokens

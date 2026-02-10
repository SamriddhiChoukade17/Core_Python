class LogInException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

LoginId = 'Admin'
Password = 'Admin'

try:
    if LoginId == "Admin" and Password == 'Admin':
        print("Valid User")

    else:
        raise LogInException("Invalid User")

except LogInException as e:
    print('Login exception', e)

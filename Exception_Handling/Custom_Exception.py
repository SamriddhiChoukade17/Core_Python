class LogInException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

#LoginId = 'Admin'
#Password = 'Admin'

try:
    LoginId = str(input("Enter login Id: "))
    Password = str(input("Enter password: "))

    if LoginId == 'Admin' and Password == 'Admin':
        raise LogInException("Invalid User")

    #else:
        #raise LogInException("Invalid User")

except LogInException as e:
    print('Login exception', e)
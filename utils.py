import re
from validate_email import validate_email

pass_reguex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{8,}$"
user_reguex = "^[a-zA-Z0-9_.-]+$"
F_ACTIVE = 'ACTIVE'
F_INACTIVE = 'INACTIVE'
EMAIL_APP = 'EMAIL_APP'
REQ_ACTIVATE = 'REQ_ACTIVATE'
REQ_FORGOT = 'REQ_FORGOT'
U_UNCONFIRMED = 'UNCONFIRMED'
U_CONFIRMED = 'CONFIRMED'


def isEmailValid(email):
    is_valid = validate_email(email)

    return is_valid


def isUsernameValid(user):
    if re.search(user_reguex, user):
        return True
    else:
        return False


def isPasswordValid(password):
    if re.search(pass_reguex, password):
        return True
    else:
        return False

def userLoggin(user_email_name, user_pass, users_data = []):
    # Comprueba los datos ingresados por el usuario.
    name_probe = "JuanMiguel" # Atributos del objeto usuario.
    email_probe = "juan@correo.com"
    pass_probe = "JuanMiguel"
    comprobacion = (user_email_name == email_probe or user_email_name == name_probe) and user_pass == pass_probe
    if comprobacion:
        return True
    else:
        return False   

def searchEmail(user_email, email_list =[]):
    email_probe = "juan@correo.com"
    print('Buscando correo')
    if (user_email == email_probe):
        return True
    return False 
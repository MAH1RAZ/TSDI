from sys import path
#path.append("/home/karim/TSDI/tp_TSDI_PY")
from form_admin import FormAdmin
from user import User


class Admin(User):
    def __init__(self, login, pwd):
        super().__init__(login, pwd)

    def afficher(self):
        FormAdmin()

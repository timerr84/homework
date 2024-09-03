class User:
    """
    класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirt):
        self.username = username
        if password == password_confirt:
            self.password = password
        else: self.password = None

class Database:
    def __init__(self):
        self.date = {}
    def add_user(self, username,password):
        self.date[username] = password
if __name__ == '__main__':
    database = Database()
    user = User(input('введите логин'), input('введите пароль'), input('повторить пароль'))
    database.add_user(user.username, user.password)
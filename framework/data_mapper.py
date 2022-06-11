import sqlite3
from abc import ABC, abstractmethod


class DataMapper(ABC):

    @abstractmethod
    def insert(self, data):
        pass


    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass


class UserMapper(DataMapper):
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):

        self.connection = connection
        self.cursor = connection.cursor()


    def get_list(self):

        statement = "SELECT LOGIN FROM USERS"
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return ()


    def find_by_login(self, login):

        statement = "SELECT LOGIN, PASSWORD FROM USERS WHERE LOGIN =?"
        self.cursor.execute(statement, (login,))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return None

    def insert(self, user):

        for key, value in user.items():
            try:
                statement = "INSERT INTO USERS (LOGIN, PASSWORD) VALUES (?, ?)"
                self.cursor.execute(statement, (key, value))
            except Exception as e:
                print(e)
            try:
                self.connection.commit()
            except Exception as e:
                print(e)

    def update(self, user):

        for key, value in user.items():
            try:
                statement = "UPDATE USERS SET PASSWORD=? WHERE LOGIN=?"
                self.cursor.execute(statement, (value, key))
            except Exception as e:
                print(e)
            try:
                self.connection.commit()
            except Exception as e:
                print(e)

    def delete(self, user):

        for key, value in user.items():
            try:
                statement = "DELETE FROM USERS WHERE LOGIN=?"
                self.cursor.execute(statement, (key,))
            except Exception as e:
                print(e)
            try:
                self.connection.commit()
            except Exception as e:
                print(e)


class AuthMapper(DataMapper):
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):

        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_addr(self, addr):
        statement = "SELECT ADDR, USER FROM AUTHENTICATION WHERE ADDR =?"
        self.cursor.execute(statement, (addr,))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return None

    def insert(self, auth):

        for key, value in auth.items():
            try:
                statement = "INSERT INTO AUTHENTICATION (ADDR, USER) VALUES (?, ?)"
                self.cursor.execute(statement, (key, value))
            except Exception as e:
                print(e)
            try:
                self.connection.commit()
            except Exception as e:
                print(e)

    def update(self, auth):
        pass

    def delete(self, addr):
        try:
            statement = "DELETE FROM AUTHENTICATION WHERE ADDR=?"
            self.cursor.execute(statement, (addr,))
        except Exception as e:
            print(e)
        try:
            self.connection.commit()
        except Exception as e:
            print(e)


# user = UserMapper(sqlite3.connect('project_db'))
# # user.insert({'test2': 11})
# t = user.get_list()
# for i in t:
#     print(i[0])
# # user.update({'test2': 13})
# # user.delete({'test2': 12})
# # print(user.find_by_login('test2'))


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


class CategoryMapper(DataMapper):
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):

        self.connection = connection
        self.cursor = connection.cursor()

    def get_id_by_category(self, category):
        statement = "SELECT ID FROM CATEGORIES WHERE CATEGORY = ?"
        self.cursor.execute(statement, (category,))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return ()

    def get_list(self):

        statement = "SELECT ID, CATEGORY FROM CATEGORIES"
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return ()

    def insert(self, category):

        try:
            statement = "INSERT INTO CATEGORIES (CATEGORY) VALUES (?)"
            self.cursor.execute(statement, (category,))
        except Exception as e:
            print(e)
        try:
            self.connection.commit()
        except Exception as e:
            print(e)

    def update(self, category):
        pass

    def delete(self, category):
        try:
            statement = "DELETE FROM CATEGORIES WHERE CATEGORY=?"
            self.cursor.execute(statement, (category,))
        except Exception as e:
            print(e)
        try:
            self.connection.commit()
        except Exception as e:
            print(e)


class CourseMapper(DataMapper):
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):

        self.connection = connection
        self.cursor = connection.cursor()

    def get_id_by_category_id_name(self, category, name):
        statement = "SELECT ID FROM COURSES WHERE CATEGORY_ID = ? AND NAME = ?"
        self.cursor.execute(statement, (category, name))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return ()

    def get_list(self):

        statement = "SELECT CATEGORY, NAME FROM COURSES, CATEGORIES WHERE COURSES.CATEGORY_ID = CATEGORIES.ID"
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        courses = {}
        for i in result:
            if i[0] in courses:
                courses[i[0]].append(i[1])
            else:
                courses[i[0]] = [i[1]]
        print(courses)
        if courses:
            return courses
        else:
            return {}

    def insert(self, course):

        try:
            statement = "INSERT INTO COURSES (NAME, CATEGORY_ID) VALUES (?, ?)"
            self.cursor.execute(statement, course)
        except Exception as e:
            print(e)
        try:
            self.connection.commit()
        except Exception as e:
            print(e)

    def update(self, course):
        pass

    def delete(self, course):
        pass

class CourseUserMapper(DataMapper):
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):

        self.connection = connection
        self.cursor = connection.cursor()

    def get_list_by_id(self, user):

        statement = "SELECT COURSE_ID FROM USERS_COURSES WHERE USER_ID = ?"
        self.cursor.execute(statement, (user,))
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return ()

    def get_list(self):

        statement = "SELECT USER_ID, COURSE_ID FROM USERS_COURSES"
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return ()

    def insert(self, course):

        try:
            statement = "INSERT INTO USERS_COURSES (USER_ID, COURSE_ID) VALUES (?, ?)"
            print(course)
            self.cursor.execute(statement, course)
        except Exception as e:
            print(e)
        try:
            self.connection.commit()
        except Exception as e:
            print(e)

    def update(self, course):
        pass

    def delete(self, course):
        pass
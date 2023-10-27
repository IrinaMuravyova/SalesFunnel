import sqlite3

class Database:
    def __init__(self, db_path: str = 'clients.db'):
        self.db_path = db_path
    
    @property # взаимодействуем с подключением как со свойством
    def connection(self):
        return sqlite3.connect(self.db_path)
    
    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data=cursor.fetchall()
        connection.close()
        return data
    #TODO: сделать это асинхронно через серверную БД

    # таблица пользователей
    def create_table_users(self):
        sql="""
        CREATE TABLE Users(
        id int NOT NULL,
        age_category_id int,
        goal_id int
        status_id int,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    # таблица возрастных категорий
    def create_table_age_categorys(self):
        sql="""
        CREATE TABLE AgeCategories(
        id int NOT NULL,
        age_category text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    # таблица целей обучения
    def create_table_goals(self):
        sql="""
        CREATE TABLE Goals(
        id int NOT NULL,
        goal text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    # таблица статусов
    def create_table_statuses(self):
        sql="""
        CREATE TABLE Statuses(
        id int NOT NULL,
        status text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)


    # добавление пользователя в таблицу пользователей
    def add_user(self, id: int, age_category_id: int = None, goal_id: int = None, status_id: int = None):
            sql = f'INSERT INTO Users(id, age_category_id, goal_id, status_id) VALUES(?,?,?,?)'
            parameters = (id, age_category_id, goal_id, status_id)
            self.execute(sql, parameters, commit=True)

    # добавление возратной категории в таблицу возрастных категорий
    def add_age_category(self, id: int, age_category: str):
            sql = f'INSERT INTO AgeCategories(id, age_category) VALUES(?,?)'
            parameters = (id, age_category)
            self.execute(sql, parameters, commit=True)

    # добавление цели в таблицу целей обучения
    def add_goal(self, id: int, goal: str):
            sql = f'INSERT INTO Goals(id, goal) VALUES(?,?)'
            parameters = (id, goal)
            self.execute(sql, parameters, commit=True)

    # добавление статуса в таблицу статусов
    def add_status(self, id: int, status: str):
            sql = f'INSERT INTO Statuses(id, status) VALUES(?,?)'
            parameters = (id, status)
            self.execute(sql, parameters, commit=True)

    # установка статуса видео для пользователя
    def set_status(self, **kwargs):
            sql = f'UPDATE Users SET status_id WHERE '
            parameters = self.format_args(sql, kwargs)
            self.execute(sql, parameters, commit=True)

    # получение статуса видео для пользователя
    def get_status_from_user(self, **kwargs)-> list:
        sql = 'SELECT status_id FROM Users WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    # показывает все записи таблицы Users
    def show_users(self):
        sql = f'SELECT * FROM Users)'
        return self.execute(sql, fetchall=True)
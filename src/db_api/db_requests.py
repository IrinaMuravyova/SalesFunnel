import sqlite3
# from loader import db

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

    @staticmethod
    def format_args(sql, parameters: dict)-> tuple: # аккуратно формируем sql команду с параметрами, чтобы случайно на их место не передать никакие функции
        # for item in parameters: print(f"item ={item}")
        # print(f"parameters = {parameters}")
        # print(f"tuple(parameters) = {tuple(parameters)}")
        # print(f"parameters.values() = {parameters.values()}")
        sql += ' AND '.join([
            f'{item} = ?' for item in parameters
        ])
        # print(f"sql = {sql}")
        return sql, tuple(parameters.values())
    
    # таблица пользователей
    def create_table_users(self):
        sql="""
        CREATE TABLE Users(
        id int NOT NULL,
        age_category_id int,
        goal_id int,
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
    
    # получение индекса возратной категории
    @staticmethod
    def get_index_of_age_category(self, **kwargs)-> list:
            sql = f'SELECT id FROM AgeCategories WHERE '
            sql, parameters = self.format_args(sql, kwargs)
            print(f"parameters of get_index = {parameters}")
            # print(f"self.execute(sql, parameters, fetchone=True) = {self.execute(sql, parameters, fetchone=True)[0]}")
            return self.execute(sql, parameters, fetchone=True)[0]

    # установка выбранной возрастной категории для пользователя
    def set_age_category(self, age_category: str, **kwargs):
            age_category_id = self.get_index_of_value(self, table="AgeCategories", age_category = age_category)
            # print(f"age_category_id = {age_category_id}")
            sql = f'UPDATE Users SET age_category_id={age_category_id} WHERE '
            # print(f"sql = {sql}")
            sql, parameters = self.format_args(sql, kwargs)
            # print(f"kwargs = {kwargs}")
            # print(f"parameters = {parameters}")
            self.execute(sql, parameters, commit=True)
            # print(f"sql = {sql}")

    # добавление цели в таблицу целей обучения
    def add_goal(self, id: int, goal: str):
            sql = f'INSERT INTO Goals(id, goal) VALUES(?,?)'
            parameters = (id, goal)
            self.execute(sql, parameters, commit=True)
    
    # получение индекса возратной категории
    @staticmethod
    def get_index_of_goal(self, **kwargs)-> list:
            sql = f'SELECT id FROM Goals WHERE '
            sql, parameters = self.format_args(sql, kwargs)
            print(f"parameters of get_index = {parameters}")
            # print(f"self.execute(sql, parameters, fetchone=True) = {self.execute(sql, parameters, fetchone=True)[0]}")
            return self.execute(sql, parameters, fetchone=True)[0]
    
    @staticmethod
    def get_index_of_value(self, table: str, **kwargs)-> list:
            sql = f'SELECT id FROM {table} WHERE '
            sql, parameters = self.format_args(sql, kwargs)
            print(f"parameters of get_index = {parameters}")
            # print(f"self.execute(sql, parameters, fetchone=True) = {self.execute(sql, parameters, fetchone=True)[0]}")
            return self.execute(sql, parameters, fetchone=True)[0]
    
    # установка цели изучения языка для пользователя
    def set_goal_id(self, goal: str, **kwargs):
            goal_id = self.get_index_of_value(self, table="Goals", goal = goal)
            # print(f"age_category_id = {goal_id}")
            sql = f'UPDATE Users SET goal_id={goal_id} WHERE '
            # print(f"sql = {sql}")
            sql, parameters = self.format_args(sql, kwargs)
            # print(f"kwargs = {kwargs}")
            # print(f"parameters = {parameters}")
            self.execute(sql, parameters, commit=True)
            # print(f"sql = {sql}")

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
        sql = f'SELECT * FROM Users'
        return self.execute(sql, fetchall=True)
    
    # показывает все записи таблицы AgeCategories
    def show_age_categories(self):
        sql = f'SELECT * FROM AgeCategories'
        return self.execute(sql, fetchall=True)
    
    # показывает все записи таблицы Goals
    def show_goals(self):
        sql = f'SELECT * FROM Goals'
        return self.execute(sql, fetchall=True)
    
    def select_data_of_table(self, table: str):
        sql = f'SELECT * FROM {table}'
        return self.execute(sql, fetchall=True)